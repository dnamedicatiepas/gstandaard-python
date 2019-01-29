from model import bst_685, bst_690, bst_691, bst_695
from wes import group_dict
from db import session


from traversal import trav_prot

all_fg_protocols = session.query(bst_690).\
            join(bst_691, bst_690.mfbpnr==bst_691.mfbpnr).\
            join(bst_695, bst_691.mfbvnr==bst_695.mfbvnr).\
            join(bst_685, bst_695.mfbpanr==bst_685.mfbpanr).\
            filter(bst_685.mfbpaoms.like('FG:%')).all()
print(len(all_fg_protocols))
print(len(set(all_fg_protocols)))


def tsitnr2mfbpanrs(session, tsitnr):
    result = session.query(bst_685).filter_by(mfbpitnr=tsitnr).all()
    return [x.mfbpanr for x in result]


results = {}
answers = {}
unknown = 0
known = 0
for sample in group_dict:    
    sample_result = 0
    for tsitnr in group_dict[sample]:
        
        if tsitnr in answers:
            tsitnr_result = answers[tsitnr]
        else:        
            tsitnr_result = 0

            try:
                sample_params = tsitnr2mfbpanrs(session, tsitnr)
            except:
                # No parameter found?
                unknown += 1
                print('unknown')
                continue

            for protocol in all_fg_protocols:
                score_teller = 0
                doorlopen_pad = []
                
                # Alleen voor testapotheken
                if protocol.mfbpwin == 'J':
                    continue
                    
                ret = trav_prot(protocol.flow, sample_params, score_teller, doorlopen_pad, debug=True)
                
                # print('Score teller: %d' % score_teller)
                print('Doorlopen pad:', doorlopen_pad)

                if ret:
                    tsitnr_result += 1
        
            answers[tsitnr] = tsitnr_result

        sample_result += tsitnr_result
        known += 1

    results[sample] = sample_result

assert len(results) == 1355
assert sum([results[x] > 0 for x in results]) == 1144
