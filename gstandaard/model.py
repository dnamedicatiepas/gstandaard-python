#
# !!!! this file is auto-generated !!!
#

from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()


class bst_685(Base):
    """Title: Bestandsbeschrijvingen: Bestand 685 MFB: Parameters"""
    __tablename__ = "bst_685"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbvnopn = Column(Integer)
    mfbvnwyz = Column(Integer)
    mfbvnvv = Column(Integer)
    mfbpaoms = Column(String(80))
    mfbpavt = Column(Integer)
    thmfbp = Column(Integer)
    mfbpitnr = Column(Integer)
    thmodu = Column(Integer)
    txmodu = Column(Integer)
    mfbpanr = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Parameters(%d)[mutkod=%s, mfbvnopn=%s, mfbvnwyz=%s, mfbvnvv=%s, mfbpaoms=%s, mfbpavt=%s, thmfbp=%s, mfbpitnr=%s, thmodu=%s, txmodu=%s, mfbpanr=%s]>" % (self.bstnum, self.mutkod, self.mfbvnopn, self.mfbvnwyz, self.mfbvnvv, self.mfbpaoms, self.mfbpavt, self.thmfbp, self.mfbpitnr, self.thmodu, self.txmodu, self.mfbpanr)

    thesaurus = relationship("bst_902")

    __table_args__ = (
        ForeignKeyConstraint(
            ['thmfbp', 'mfbpitnr'],
            ['bst_902.tsnr', 'bst_902.tsitnr'],
        ),
    )


class bst_686(Base):
    """Title: Bestandsbeschrijvingen: Bestand 686 MFB: Attributen"""
    __tablename__ = "bst_686"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbattyp = Column(Integer)
    mfbvnopn = Column(Integer)
    mfbvnwyz = Column(Integer)
    mfbvnvv = Column(Integer)
    mfbatoms = Column(String(80))
    thmfbp = Column(Integer)
    mfbpitnr = Column(Integer)
    thmodu = Column(Integer)
    txmodu = Column(Integer)
    mfbatnr = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Attributen(%d)[mutkod=%s, mfbattyp=%s, mfbvnopn=%s, mfbvnwyz=%s, mfbvnvv=%s, mfbatoms=%s, thmfbp=%s, mfbpitnr=%s, thmodu=%s, txmodu=%s, mfbatnr=%s]>" % (self.bstnum, self.mutkod, self.mfbattyp, self.mfbvnopn, self.mfbvnwyz, self.mfbvnvv, self.mfbatoms, self.thmfbp, self.mfbpitnr, self.thmodu, self.txmodu, self.mfbatnr)


class bst_689(Base):
    """Title: Bestandsbeschrijvingen: Bestand 689 MFB: Functie"""
    __tablename__ = "bst_689"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbvnopn = Column(Integer)
    mfbvnwyz = Column(Integer)
    mfbvnvv = Column(Integer)
    mfbfuoms = Column(String(80))
    thmodu = Column(Integer)
    txmodu = Column(Integer)
    mfbfunnr = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Functie(%d)[mutkod=%s, mfbvnopn=%s, mfbvnwyz=%s, mfbvnvv=%s, mfbfuoms=%s, thmodu=%s, txmodu=%s, mfbfunnr=%s]>" % (self.bstnum, self.mutkod, self.mfbvnopn, self.mfbvnwyz, self.mfbvnvv, self.mfbfuoms, self.thmodu, self.txmodu, self.mfbfunnr)


class bst_690(Base):
    """Title: Bestandsbeschrijvingen: Bestand 690 MFB: Protocol"""
    __tablename__ = "bst_690"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbpdvv = Column(Integer)
    mfbpoms = Column(String(80))
    mfbpwin = Column(String(1))
    thmfbb = Column(Integer)
    mfbbron = Column(Integer)
    mfbpwind = Column(Integer)
    mfbknr = Column(Integer)
    thmodu = Column(Integer)
    txmodu = Column(Integer)
    mfbpnr = Column(Integer, primary_key=True)
    mfbpnrv = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Protocol(%d)[mutkod=%s, mfbpdvv=%s, mfbpoms=%s, mfbpwin=%s, thmfbb=%s, mfbbron=%s, mfbpwind=%s, mfbknr=%s, thmodu=%s, txmodu=%s, mfbpnr=%s, mfbpnrv=%s]>" % (self.bstnum, self.mutkod, self.mfbpdvv, self.mfbpoms, self.mfbpwin, self.thmfbb, self.mfbbron, self.mfbpwind, self.mfbknr, self.thmodu, self.txmodu, self.mfbpnr, self.mfbpnrv)

    flow = relationship("bst_691")

    __table_args__ = (
        ForeignKeyConstraint(
            ['mfbknr', 'mfbpnr'],
            ['bst_691.mfbknr', 'bst_691.mfbpnr'],
        ),
    )


class bst_691(Base):
    """Title: Bestandsbeschrijvingen: Bestand 691 MFB: Protocol flow"""
    __tablename__ = "bst_691"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbpjk = Column(Integer, ForeignKey("bst_691.mfbknr"))
    mfbpja = Column(Integer, ForeignKey("bst_693.mfbanr"))
    mfbpnk = Column(Integer, ForeignKey("bst_691.mfbknr"))
    mfbpna = Column(Integer, ForeignKey("bst_693.mfbanr"))
    mfbvnr = Column(Integer, ForeignKey("bst_692.mfbvnr"))
    mfbpnr = Column(Integer, primary_key=True)
    mfbpnrv = Column(Integer, primary_key=True)
    mfbknr = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Protocol flow(%d)[mutkod=%s, mfbpjk=%s, mfbpja=%s, mfbpnk=%s, mfbpna=%s, mfbvnr=%s, mfbpnr=%s, mfbpnrv=%s, mfbknr=%s]>" % (self.bstnum, self.mutkod, self.mfbpjk, self.mfbpja, self.mfbpnk, self.mfbpna, self.mfbvnr, self.mfbpnr, self.mfbpnrv, self.mfbknr)

    vraag = relationship("bst_692")
    ja_flow = relationship('bst_691', primaryjoin='and_(bst_691.mfbpjk==bst_691.mfbknr, bst_691.mfbpnr==bst_691.mfbpnr)', remote_side=[mfbknr, mfbpnr])
    nee_flow = relationship('bst_691', primaryjoin='and_(bst_691.mfbpnk==bst_691.mfbknr, bst_691.mfbpnr==bst_691.mfbpnr)', remote_side=[mfbknr, mfbpnr])
    ja_actie = relationship('bst_693', primaryjoin='bst_691.mfbpja==bst_693.mfbanr')
    nee_actie = relationship('bst_693', primaryjoin='bst_691.mfbpna==bst_693.mfbanr')


class bst_692(Base):
    """Title: Bestandsbeschrijvingen: Bestand 692 MFB: Vragen"""
    __tablename__ = "bst_692"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbvoms = Column(String(80))
    mfbfuwo = Column(Integer)
    mfbfunnr = Column(Integer, ForeignKey("bst_689.mfbfunnr"))
    mfbvstj = Column(Integer)
    mfbvstjt = Column(String(80))
    mfbvstn = Column(Integer)
    mfbvstnt = Column(String(80))
    mfbvoper = Column(String(2))
    mfbvw = Column(Integer)
    mfbvnr = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Vragen(%d)[mutkod=%s, mfbvoms=%s, mfbfuwo=%s, mfbfunnr=%s, mfbvstj=%s, mfbvstjt=%s, mfbvstn=%s, mfbvstnt=%s, mfbvoper=%s, mfbvw=%s, mfbvnr=%s]>" % (self.bstnum, self.mutkod, self.mfbvoms, self.mfbfuwo, self.mfbfunnr, self.mfbvstj, self.mfbvstjt, self.mfbvstn, self.mfbvstnt, self.mfbvoper, self.mfbvw, self.mfbvnr)

    functie = relationship("bst_689")
    vraag_functie_parameter = relationship('bst_695')
    vraag_functie_waardelijst = relationship('bst_696')
    vraag_functie_attribuut = relationship('bst_697')

    parameters = association_proxy("vraag_functie_parameter", "parameter")
    waardelijsten = association_proxy("vraag_functie_waardelijst", "waardelijst")
    attributen = association_proxy("vraag_functie_attribuut", "attribuut")


class bst_693(Base):
    """Title: Bestandsbeschrijvingen: Bestand 693 MFB: Actie"""
    __tablename__ = "bst_693"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbaoms = Column(String(80))
    mfbajn = Column(String(1))
    mfbmon = Column(String(1))
    thmodu = Column(Integer)
    txmodu = Column(Integer, ForeignKey("bst_921.txmodu"))
    mfbanr = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Actie(%d)[mutkod=%s, mfbaoms=%s, mfbajn=%s, mfbmon=%s, thmodu=%s, txmodu=%s, mfbanr=%s]>" % (self.bstnum, self.mutkod, self.mfbaoms, self.mfbajn, self.mfbmon, self.thmodu, self.txmodu, self.mfbanr)

    teksten = relationship('bst_921', uselist=True, primaryjoin='and_(bst_693.mfbanr==bst_921.txkode, bst_693.txmodu==bst_921.txmodu, 240==bst_921.txtsrt)')
    bouwstenen = relationship("bst_694")

    @hybrid_property
    def tekst(self):
        return [x.txtext for x in self.teksten]


class bst_694(Base):
    """Title: Bestandsbeschrijvingen: Bestand 694 MFB: Actie - Parameter"""
    __tablename__ = "bst_694"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbanr = Column(Integer, ForeignKey("bst_693.mfbanr"), primary_key=True)
    mfbnr = Column(Integer, primary_key=True)
    mfbaanst = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Actie - Parameter(%d)[mutkod=%s, mfbanr=%s, mfbnr=%s, mfbaanst=%s]>" % (self.bstnum, self.mutkod, self.mfbanr, self.mfbnr, self.mfbaanst)


class bst_695(Base):
    """Title: Bestandsbeschrijvingen: Bestand 695 MFB: Vraag - Functie - Parameter"""
    __tablename__ = "bst_695"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbpanr = Column(Integer, ForeignKey("bst_685.mfbpanr"))
    mfbvnr = Column(Integer, ForeignKey("bst_692.mfbvnr"), primary_key=True)
    mfbfunnr = Column(Integer, ForeignKey("bst_689.mfbfunnr"), primary_key=True)
    mfbfuns1 = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Vraag - Functie - Parameter(%d)[mutkod=%s, mfbpanr=%s, mfbvnr=%s, mfbfunnr=%s, mfbfuns1=%s]>" % (self.bstnum, self.mutkod, self.mfbpanr, self.mfbvnr, self.mfbfunnr, self.mfbfuns1)

    vraag = relationship("bst_692")
    functie = relationship("bst_689")
    parameter = relationship("bst_685")


class bst_696(Base):
    """Title: Bestandsbeschrijvingen: Bestand 696 MFB: Vraag - Functie - Waardelijst"""
    __tablename__ = "bst_696"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbwnr = Column(Integer, ForeignKey("bst_699.mfbwnr"))
    mfbvopew = Column(String(2))
    mfbvnr = Column(Integer, ForeignKey("bst_692.mfbvnr"), primary_key=True)
    mfbfunnr = Column(Integer, ForeignKey("bst_689.mfbfunnr"), primary_key=True)
    mfbfuns2 = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Vraag - Functie - Waardelijst(%d)[mutkod=%s, mfbwnr=%s, mfbvopew=%s, mfbvnr=%s, mfbfunnr=%s, mfbfuns2=%s]>" % (self.bstnum, self.mutkod, self.mfbwnr, self.mfbvopew, self.mfbvnr, self.mfbfunnr, self.mfbfuns2)

    vraag = relationship("bst_692")
    functie = relationship("bst_689")
    waardelijst = relationship("bst_699")


class bst_697(Base):
    """Title: Bestandsbeschrijvingen: Bestand 697 MFB: Vraag - Functie - Attribuut"""
    __tablename__ = "bst_697"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbatnr = Column(Integer, ForeignKey("bst_686.mfbatnr"))
    mfbfuwt = Column(Integer)
    mfbvnr = Column(Integer, ForeignKey("bst_692.mfbvnr"), primary_key=True)
    mfbfunnr = Column(Integer, ForeignKey("bst_689.mfbfunnr"), primary_key=True)
    mfbfuns3 = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<MFB: Vraag - Functie - Attribuut(%d)[mutkod=%s, mfbatnr=%s, mfbfuwt=%s, mfbvnr=%s, mfbfunnr=%s, mfbfuns3=%s]>" % (self.bstnum, self.mutkod, self.mfbatnr, self.mfbfuwt, self.mfbvnr, self.mfbfunnr, self.mfbfuns3)

    vraag = relationship("bst_692")
    functie = relationship("bst_689")
    attribuut = relationship("bst_686")


class bst_699(Base):
    """Title: Bestandsbeschrijvingen: Bestand 699 MFB: Waardelijsten meerdere niveaus"""
    __tablename__ = "bst_699"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    mfbwoms = Column(String(80))
    thsrtcde = Column(Integer)
    mfbwnr = Column(Integer, primary_key=True)
    srtcode = Column(Integer, primary_key=True)
    codenv = Column(String(10), primary_key=True)

    def __repr__(self):
        return "<MFB: Waardelijsten meerdere niveaus(%d)[mutkod=%s, mfbwoms=%s, thsrtcde=%s, mfbwnr=%s, srtcode=%s, codenv=%s]>" % (self.bstnum, self.mutkod, self.mfbwoms, self.thsrtcde, self.mfbwnr, self.srtcode, self.codenv)


class bst_902(Base):
    """Title: Bestandsbeschrijvingen: Bestand 902 Thesauri totaal"""
    __tablename__ = "bst_902"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    thitmk = Column(String(2))
    thnm4 = Column(String(4))
    thnm15 = Column(String(15))
    thnm25 = Column(String(25))
    thnm50 = Column(String(50))
    thakd1 = Column(String(1))
    thakd2 = Column(String(1))
    thakd3 = Column(String(1))
    thakd4 = Column(String(1))
    thakd5 = Column(String(1))
    thakd6 = Column(String(1))
    tsnr = Column(Integer, primary_key=True)
    tsitnr = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Thesauri totaal(%d)[mutkod=%s, thitmk=%s, thnm4=%s, thnm15=%s, thnm25=%s, thnm50=%s, thakd1=%s, thakd2=%s, thakd3=%s, thakd4=%s, thakd5=%s, thakd6=%s, tsnr=%s, tsitnr=%s]>" % (self.bstnum, self.mutkod, self.thitmk, self.thnm4, self.thnm15, self.thnm25, self.thnm50, self.thakd1, self.thakd2, self.thakd3, self.thakd4, self.thakd5, self.thakd6, self.tsnr, self.tsitnr)


class bst_921(Base):
    """Title: Bestandsbeschrijvingen: Bestand 921 Tekstblokken ASCII (vervangt 920)"""
    __tablename__ = "bst_921"

    bstnum = Column(Integer)
    mutkod = Column(Integer)
    thmodu = Column(Integer)
    thtsrt = Column(Integer)
    txtext = Column(String(132))
    txmodu = Column(Integer, primary_key=True)
    txtsrt = Column(Integer, primary_key=True)
    txkode = Column(Integer, primary_key=True)
    txblnr = Column(Integer, primary_key=True)
    txrgln = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Tekstblokken ASCII (vervangt 920)(%d)[mutkod=%s, thmodu=%s, thtsrt=%s, txtext=%s, txmodu=%s, txtsrt=%s, txkode=%s, txblnr=%s, txrgln=%s]>" % (self.bstnum, self.mutkod, self.thmodu, self.thtsrt, self.txtext, self.txmodu, self.txtsrt, self.txkode, self.txblnr, self.txrgln)

