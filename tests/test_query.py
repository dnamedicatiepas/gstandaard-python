from gstandaard.model import bst_685, bst_690, bst_691, bst_695
from gstandaard.wes import group_dict
from gstandaard.db import session
from gstandaard.traversal import trav_prot, tsitnr2mfbpanrs


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
