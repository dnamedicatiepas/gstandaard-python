# TODO: Bepaal mbv bestand 682 welke interacties, contra-indicaties, dubbelmedicaties, leeftijd als CI 
# (op basis van thes.17) en meldingen van bijzondere kenmerken niet meer hoeven te worden uitgevoerd.

from .constants import ATTRIBUUT_GETAL, FUNCTIE_CI_AARD, THAKD4_F, TSNR_CI
from .model import bst_685, bst_690, bst_691, bst_692, bst_695

def aanwezigheid_parameter_waardelijst(naald, hooiberg):
    if naald in hooiberg:
        return 100
    return 0


attribuut_functies = {
    4: aanwezigheid_parameter_waardelijst,
}
# attribuut_functies[4](3, (1, 2))

operators = {
    '=': (lambda x, y: x == y)
}
# operators['='](True, True)


def tsitnr2mfbpanrs(session, tsitnr):
    result = session.query(bst_685).filter_by(mfbpitnr=tsitnr).all()
    return [x.mfbpanr for x in result]


def get_protocols(session, fg_only=False):
    # Protocols -> Flow -> Vraag -> Vraag_Functie_Parameter -> Parameter
    protocols = session.query(bst_690).join(bst_691).join(bst_692).join(bst_695).join(bst_685)

    if fg_only:
        return protocols.filter(bst_685.thesaurus.has(tsnr=TSNR_CI, thakd4=THAKD4_F)).all()

    return protocols.all()


def trav_actie(actie, debug=False):
    
    # TODO: moet er nog iets met 694/bouwsteen/vervolg actie gebeuren?
    if len(actie.bouwstenen) > 0:
        raise NotImplementedError('No follow-up action/bouwstenen functionality implemented')

    if actie.mfbajn == 'J':
        desc = '\n'.join(actie.tekst)
        if debug:
            print('DESC:', desc)
        return True
    
    else:
        if debug:
            print('Geen actie:', actie.mfbaoms)
        return False


def trav_prot(flow, sample_params, doorlopen_pad, debug=False):
    
    # Vragen zijn onderdeel van een knooppunt in het protocol (zie bst 691).
    # Het antwoord op de vraag (ja of nee) bepaalt het vervolgknooppunt binnen het protocol.
    # Vragen bevatten in principe een functies, attributen en zo nodig parameters en/of waardenlijsten.
    # Vragen die geen functie, attribuut, parameter of waardenlijst hebben, bevatten een protocolattribuut.
    
    if debug:
        print('protocol flow:', flow.mfbpnr)
        print('knoop nummer:', flow.mfbknr)
        
    vraag = flow.vraag
    
    if debug:
        print('Vraagnummer: %s' % vraag.mfbvnr)
        print('Vraag omschrijving:', vraag.mfbvoms)
        print('Vraag operator:', vraag.mfbvoper)

        # TODO: deal better with decimal values
        print('Vraag waarde: %d' % vraag.mfbvw)
                        
    # We don't have code to deal with protocol attributes
    # (Geen eerder berekend resultaat gebruiken.)
    if vraag.mfbfuwo > 0:
        raise NotImplementedError('No code for dealing with protocol attributes (%d)' % vraag.mfbfuwo)
    
    # Validate that questions have a function (we ignored attributed above ...)
    if vraag.mfbfunnr == 0:
        raise ValueError('No function defined')
    
    if debug:
        print('Functie omschrijving: %s' % vraag.functie.mfbfuoms)
    
    # We can only deal with "Zoek naar een bepaalde CI-aard bij de patient"?!
    if vraag.mfbfunnr != FUNCTIE_CI_AARD:
        raise RuntimeWarning('Function not implemented "%d:%s"' % (vraag.mfbfunnr, vraag.functie.mfbfuoms))

    # "Door MFBFUNS1 kunnen meerdere parameters aan een functie (bij een specifieke vraag) gekoppeld worden."
    if len(vraag.parameters) != 1:
        raise ValueError('Dont know how to handle %d parameters' % len(vraag.parameters))
    parameter = vraag.parameters[0]
    if debug:
        print('Parameter:', parameter.mfbpanr, parameter.mfbpaoms)
        print('Sample parameters: %s' % sample_params)
        
    # "Door MFBFUNS2 kunnen meerdere waardenlijsten aan een functie (bij een specifieke vraag) gekoppeld worden."
    # Vooralsnog altijd leeg in onze data
    if len(vraag.waardelijsten) > 0:
        raise NotImplementedError("Waardelijsten not implemented")
   
    # "Door MFBFUNS3 kunnen meerdere attributen aan een functie (bij een specifieke vraag) gekoppeld worden."
    # Kunnen er potentieel meer zijn
    if len(vraag.attributen) != 1:
        raise ValueError('Dont know how to handle %d attributes' % len(vraag.attributen))
    attribuut = vraag.attributen[0]
    if debug:
        print('Attribuut %d, %s:' % (attribuut.mfbatnr, attribuut.mfbatoms))
        print('Attribuut type: %s (%s)' % (attribuut.mfbattyp, 'GETAL' if attribuut.mfbattyp == ATTRIBUUT_GETAL else 'BOOLEAN'))

    # We don't have code to deal with protocol attributes
    if vraag.vraag_functie_attribuut[0].mfbfuwt > 0:
        raise NotImplementedError('No code for dealing with protocol attributes (%d)' % vraag.vraag_functie_attribuut[0].mfbfuwt)

    # Currently we only have one attribute function implemented
    if attribuut.mfbatnr not in [4]:
        raise NotImplementedError("No implementation for attribuut function: %d, %s" % (attribuut.mfbatnr, attribuut.mfbatoms))

    IVwaarde = attribuut_functies[attribuut.mfbatnr](parameter.mfbpanr, sample_params)   
    if debug:
        print('IVwaarde: %d' % IVwaarde)
        
    op_result = operators[vraag.mfbvoper.strip()](IVwaarde, vraag.mfbvw)
    if debug:
        print("Operator result:", op_result)
    
    if op_result:
        if vraag.mfbvstj > 0:
            raise NotImplementedError('"Scoreteller" functionality is not implemented')
        doorlopen_pad.append(vraag.mfbvstjt)

        if flow.mfbpjk:
            trav_prot(flow.ja_flow, sample_params, doorlopen_pad, debug)
        else:
            if debug:
                print('JA Actie: %s' % flow.mfbpja)
            return trav_actie(flow.ja_actie, debug)
    else:
        if vraag.mfbvstn > 0:
            raise NotImplementedError('Scoreteller is not implemented')
        doorlopen_pad.append(vraag.mfbvstnt)

        if flow.mfbpnk:
            trav_prot(flow.nee_flow, sample_params, doorlopen_pad, debug)
        else:
            if debug:
                print('NEE Actie: %s' % flow.mfbpna)
            return trav_actie(flow.nee_actie, debug)
