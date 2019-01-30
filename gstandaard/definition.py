from constants import ZIEKENHUISTEKST

foreign_keys = {
    'bst_685': [
        {
            'mfbpitnr': 'bst_902.tsitnr',
            'thmfbp': 'bst_902.tsnr'
        }
    ],

    'bst_690': [
        {
            'mfbpnr': 'bst_691.mfbpnr',
            'mfbknr': 'bst_691.mfbknr'
        }
    ],

    'bst_691': [
        {
            'mfbvnr': 'bst_692.mfbvnr'
        },
        {
            'mfbpjk': 'bst_691.mfbknr'  # nullable=True ?
        },
        {
            'mfbpnk': 'bst_691.mfbknr'  # nullable=True ?
        },
        {
            'mfbpja': 'bst_693.mfbanr'
        },
        {
            'mfbpna': 'bst_693.mfbanr'
        }

    ],

    'bst_692': [
        {
            'mfbfunnr': 'bst_689.mfbfunnr'
        }
    ],

    'bst_693': [
        {
            'txmodu': 'bst_921.txmodu'
        }
    ],

    'bst_694': [
        {
            'mfbanr': 'bst_693.mfbanr'
        }
    ],

    'bst_695': [
        {
            'mfbvnr': 'bst_692.mfbvnr',
        },
        {
            'mfbfunnr': 'bst_689.mfbfunnr',
        },
        {
            'mfbpanr': 'bst_685.mfbpanr'
        }
    ],

    'bst_696': [
        {
            'mfbvnr': 'bst_692.mfbvnr',
        },
        {
            'mfbfunnr': 'bst_689.mfbfunnr',
        },
        {
            'mfbwnr': 'bst_699.mfbwnr'
        }
    ],

    'bst_697': [
        {
            'mfbvnr': 'bst_692.mfbvnr',
        },
        {
            'mfbfunnr': 'bst_689.mfbfunnr',
        },
        {
            'mfbatnr': 'bst_686.mfbatnr'
        }
    ],

}

relationships = {
    'bst_685': {
        'thesaurus': '"bst_902"'
    },

    'bst_690': {
        'flow': '"bst_691"'
    },

    'bst_691': {
        'vraag': '"bst_692"',

        'ja_flow': 'bst_691.mfbpjk==bst_691.mfbknr, bst_691.mfbpnr==bst_691.mfbpnr',
        'nee_flow': 'bst_691.mfbpnk==bst_691.mfbknr, bst_691.mfbpnr==bst_691.mfbpnr',

        'ja_actie': "'bst_691.mfbpja==bst_693.mfbanr'",
        'nee_actie': "'bst_691.mfbpna==bst_693.mfbanr'"
    },

    'bst_692': {
        'functie': '"bst_689"',
        'vraag_functie_parameter': "'bst_695'",
        'vraag_functie_waardelijst': "'bst_696'",
        'vraag_functie_attribuut': "'bst_697'",
    },

    'bst_693': {
        'teksten': ['bst_693.mfbanr==bst_921.txkode, bst_693.txmodu==bst_921.txmodu, %s==bst_921.txtsrt' % ZIEKENHUISTEKST],
        'bouwstenen': '"bst_694"'
    },

    'bst_695': {
        'vraag': '"bst_692"',
        'functie': '"bst_689"',
        'parameter': '"bst_685"'
    },

    'bst_696': {
        'vraag': '"bst_692"',
        'functie': '"bst_689"',
        'waardelijst': '"bst_699"'
    },

    'bst_697': {
        'vraag': '"bst_692"',
        'functie': '"bst_689"',
        'attribuut': '"bst_686"'
    }
}

aggregates = {
    'bst_693': {
        'tekst': ('txtext', 'self.teksten')
    }
}

proxies = {
    'bst_692': {
        'parameters': ('vraag_functie_parameter', 'parameter'),
        'waardelijsten': ('vraag_functie_waardelijst', 'waardelijst'),
        'attributen': ('vraag_functie_attribuut', 'attribuut')
    }
}