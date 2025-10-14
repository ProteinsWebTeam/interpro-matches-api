matches = [
    {
        "md5": "023DD5D4BF9625F10F6FF028F97335DA",
        "matches": [
            {
                "signature": {
                    "accession": "G3DSA:3.40.630.30",
                    "name": None,
                    "description": None,
                    "type": "Homologous_superfamily",
                    "signatureLibraryRelease": {
                        "library": "CATH-Gene3D",
                        "version": "4.3.0",
                    },
                    "entry": None,
                },
                "modelAccession": "5c82A00",
                "score": 76.9,
                "evalue": 6.8e-21,
                "locations": [
                    {
                        "start": 9,
                        "end": 143,
                        "hmmStart": 76,
                        "hmmEnd": 173,
                        "hmmLength": 190,
                        "evalue": 7.8e-21,
                        "score": 76.7,
                        "fragments": [{"start": 9, "end": 143, "type": "CONTINUOUS"}],
                        "hmmBounds": "COMPLETE",
                        "envelopeStart": 9,
                        "envelopeEnd": 143,
                    }
                ],
                "source": "CATH-Gene3D",
            },
            {
                "signature": {
                    "accession": "cd04301",
                    "name": "NAT_SF",
                    "description": "N-Acyltransferase superfamily: Various enzymes that characteristically catalyze the transfer of an acyl group to a substrate",
                    "type": "Domain",
                    "signatureLibraryRelease": {"library": "CDD", "version": "3.21"},
                    "entry": None,
                },
                "modelAccession": "cd04301",
                "locations": [
                    {
                        "start": 50,
                        "end": 99,
                        "evalue": 4.23184e-06,
                        "score": 40.3369,
                        "fragments": [{"start": 50, "end": 99, "type": "CONTINUOUS"}],
                        "sites": [
                            {
                                "description": "Coenzyme A binding pocket",
                                "numLocations": 5,
                                "siteLocations": [
                                    {"start": 89, "end": 89, "residue": "S"},
                                    {"start": 78, "end": 78, "residue": "L"},
                                    {"start": 88, "end": 88, "residue": "G"},
                                    {"start": 77, "end": 77, "residue": "H"},
                                    {"start": 76, "end": 76, "residue": "L"},
                                ],
                            }
                        ],
                    }
                ],
                "source": "CDD",
            },
            {
                "signature": {
                    "accession": "PTHR43877",
                    "name": None,
                    "description": "AMINOALKYLPHOSPHONATE N-ACETYLTRANSFERASE-RELATED-RELATED",
                    "type": "Family",
                    "signatureLibraryRelease": {
                        "library": "PANTHER",
                        "version": "19.0",
                    },
                    "entry": {
                        "accession": "IPR050832",
                        "name": "Bact_Acetyltransf",
                        "description": "Bacterial Acetyltransferase",
                        "type": "Family",
                        "parent": None,
                    },
                },
                "modelAccession": "PTHR43877:SF2",
                "ancestralNode": "AN30",
                "evalue": 2.5e-12,
                "score": 59.0,
                "locations": [
                    {
                        "start": 31,
                        "end": 131,
                        "hmmStart": 40,
                        "hmmEnd": 144,
                        "hmmLength": 0,
                        "hmmBounds": "INCOMPLETE",
                        "envelopeStart": 8,
                        "envelopeEnd": 135,
                        "fragments": [{"start": 31, "end": 131, "type": "CONTINUOUS"}],
                    }
                ],
                "source": "PANTHER",
            },
            {
                "signature": {
                    "accession": "PS51186",
                    "name": "GNAT",
                    "description": "Gcn5-related N-acetyltransferase (GNAT) domain profile",
                    "type": "Domain",
                    "signatureLibraryRelease": {
                        "library": "PROSITE profiles",
                        "version": "2025_01",
                    },
                    "entry": {
                        "accession": "IPR000182",
                        "name": "GNAT_dom",
                        "description": "GNAT domain",
                        "type": "Domain",
                        "parent": None,
                    },
                },
                "modelAccession": "PS51186",
                "locations": [
                    {
                        "start": 3,
                        "end": 143,
                        "cigarAlignment": "36M5I4M1I67M1D21M4D7M",
                        "fragments": [{"start": 3, "end": 143, "type": "CONTINUOUS"}],
                        "score": 18.73147,
                    }
                ],
                "source": "PROSITE profiles",
            },
            {
                "signature": {
                    "accession": "PF00583",
                    "name": "Acetyltransf_1",
                    "description": "Acetyltransferase (GNAT) family",
                    "type": "Family",
                    "signatureLibraryRelease": {"library": "Pfam", "version": "38.0"},
                    "entry": {
                        "accession": "IPR000182",
                        "name": "GNAT_dom",
                        "description": "GNAT domain",
                        "type": "Domain",
                        "parent": None,
                    },
                },
                "modelAccession": "PF00583",
                "score": 49.8,
                "evalue": 1.2e-09,
                "locations": [
                    {
                        "start": 35,
                        "end": 126,
                        "hmmStart": 16,
                        "hmmEnd": 116,
                        "hmmLength": 116,
                        "evalue": 1.5e-09,
                        "score": 49.5,
                        "fragments": [{"start": 35, "end": 126, "type": "CONTINUOUS"}],
                        "hmmBounds": "C_TERMINAL_COMPLETE",
                        "envelopeStart": 14,
                        "envelopeEnd": 126,
                    }
                ],
                "source": "Pfam",
            },
            {
                "signature": {
                    "accession": "SSF55729",
                    "name": None,
                    "description": "Acyl-CoA N-acyltransferases (Nat)",
                    "type": "Homologous_superfamily",
                    "signatureLibraryRelease": {
                        "library": "SUPERFAMILY",
                        "version": "1.75",
                    },
                    "entry": {
                        "accession": "IPR016181",
                        "name": "Acyl_CoA_acyltransferase",
                        "description": "Acyl-CoA N-acyltransferase",
                        "type": "Homologous_superfamily",
                        "parent": None,
                    },
                },
                "modelAccession": "0051915",
                "evalue": 1.86e-23,
                "locations": [
                    {
                        "start": 7,
                        "end": 140,
                        "hmmLength": 167,
                        "fragments": [{"start": 7, "end": 140, "type": "CONTINUOUS"}],
                    }
                ],
                "source": "SUPERFAMILY",
            },
        ],
    },
    {
        "md5": "027B772F8CBF20AF5184B09B9CBA7602",
        "matches": [
            {
                "signature": {
                    "accession": "G3DSA:3.40.1380.10",
                    "name": None,
                    "description": None,
                    "type": "Homologous_superfamily",
                    "signatureLibraryRelease": {
                        "library": "CATH-Gene3D",
                        "version": "4.3.0",
                    },
                    "entry": None,
                },
                "modelAccession": "5fl7G02",
                "score": 332.6,
                "evalue": 8.7e-99,
                "locations": [
                    {
                        "start": 27,
                        "end": 247,
                        "hmmStart": 1,
                        "hmmEnd": 262,
                        "hmmLength": 205,
                        "evalue": 9.7e-99,
                        "score": 332.4,
                        "fragments": [{"start": 27, "end": 247, "type": "CONTINUOUS"}],
                        "hmmBounds": "INCOMPLETE",
                        "envelopeStart": 5,
                        "envelopeEnd": 286,
                    }
                ],
                "source": "CATH-Gene3D",
            },
            {
                "signature": {
                    "accession": "G3DSA:1.10.287.80",
                    "name": None,
                    "description": "ATP synthase, gamma subunit, helix hairpin domain",
                    "type": "Homologous_superfamily",
                    "signatureLibraryRelease": {
                        "library": "CATH-Gene3D",
                        "version": "4.3.0",
                    },
                    "entry": None,
                },
                "modelAccession": "5fl7G01",
                "score": 332.6,
                "evalue": 8.7e-99,
                "locations": [
                    {
                        "start": 5,
                        "end": 285,
                        "hmmStart": 1,
                        "hmmEnd": 262,
                        "hmmLength": 66,
                        "evalue": 9.7e-99,
                        "score": 332.4,
                        "fragments": [
                            {"start": 5, "end": 26, "type": "C_TERMINAL_DISC"},
                            {"start": 248, "end": 285, "type": "N_TERMINAL_DISC"},
                        ],
                        "hmmBounds": "N_TERMINAL_COMPLETE",
                        "envelopeStart": 5,
                        "envelopeEnd": 286,
                    }
                ],
                "source": "CATH-Gene3D",
            },
            {
                "signature": {
                    "accession": "Coil",
                    "name": None,
                    "description": "Coil",
                    "type": "Region",
                    "signatureLibraryRelease": {"library": "COILS", "version": "2.2.1"},
                    "entry": None,
                },
                "modelAccession": "Coil",
                "locations": [
                    {
                        "start": 252,
                        "end": 272,
                        "fragments": [{"start": 252, "end": 272, "type": "CONTINUOUS"}],
                    }
                ],
                "source": "COILS",
            },
            {
                "signature": {
                    "accession": "G3DSA:1.10.287.80:FF:000005",
                    "name": None,
                    "description": "ATP synthase gamma chain",
                    "type": "Region",
                    "signatureLibraryRelease": {
                        "library": "CATH-FunFam",
                        "version": "4.3.0",
                    },
                    "entry": None,
                },
                "modelAccession": "1.10.287.80-FF-000005",
                "score": 242.7,
                "evalue": 3.7e-72,
                "locations": [
                    {
                        "start": 2,
                        "end": 87,
                        "hmmStart": 1,
                        "hmmEnd": 63,
                        "hmmLength": 140,
                        "evalue": 1.1e-32,
                        "score": 114.9,
                        "fragments": [{"start": 2, "end": 87, "type": "CONTINUOUS"}],
                        "hmmBounds": "N_TERMINAL_COMPLETE",
                        "envelopeStart": 2,
                        "envelopeEnd": 87,
                    },
                    {
                        "start": 199,
                        "end": 288,
                        "hmmStart": 59,
                        "hmmEnd": 140,
                        "hmmLength": 140,
                        "evalue": 3e-37,
                        "score": 129.6,
                        "fragments": [{"start": 199, "end": 288, "type": "CONTINUOUS"}],
                        "hmmBounds": "C_TERMINAL_COMPLETE",
                        "envelopeStart": 199,
                        "envelopeEnd": 288,
                    },
                ],
                "source": "CATH-FunFam",
            },
            {
                "signature": {
                    "accession": "G3DSA:3.40.1380.10:FF:000001",
                    "name": None,
                    "description": "ATP synthase gamma chain",
                    "type": "Region",
                    "signatureLibraryRelease": {
                        "library": "CATH-FunFam",
                        "version": "4.3.0",
                    },
                    "entry": None,
                },
                "modelAccession": "3.40.1380.10-FF-000001",
                "score": 392.3,
                "evalue": 2e-117,
                "locations": [
                    {
                        "start": 27,
                        "end": 247,
                        "hmmStart": 1,
                        "hmmEnd": 220,
                        "hmmLength": 220,
                        "evalue": 2.4e-117,
                        "score": 392.0,
                        "fragments": [{"start": 27, "end": 247, "type": "CONTINUOUS"}],
                        "hmmBounds": "COMPLETE",
                        "envelopeStart": 27,
                        "envelopeEnd": 247,
                    }
                ],
                "source": "CATH-FunFam",
            },
            {
                "signature": {
                    "accession": "cd12151",
                    "name": "F1-ATPase_gamma",
                    "description": "mitochondrial ATP synthase gamma subunit",
                    "type": "Domain",
                    "signatureLibraryRelease": {"library": "CDD", "version": "3.21"},
                    "entry": {
                        "accession": "IPR000131",
                        "name": "ATP_synth_F1_gsu",
                        "description": "ATP synthase, F1 complex, gamma subunit",
                        "type": "Family",
                        "parent": None,
                    },
                },
                "modelAccession": "cd12151",
                "locations": [
                    {
                        "start": 2,
                        "end": 285,
                        "evalue": 3.84833e-127,
                        "score": 361.51,
                        "fragments": [{"start": 2, "end": 285, "type": "CONTINUOUS"}],
                        "sites": [
                            {
                                "description": "core domain interface",
                                "numLocations": 38,
                                "siteLocations": [
                                    {"start": 284, "end": 284, "residue": "G"},
                                    {"start": 30, "end": 30, "residue": "S"},
                                    {"start": 24, "end": 24, "residue": "M"},
                                    {"start": 267, "end": 267, "residue": "N"},
                                    {"start": 125, "end": 125, "residue": "F"},
                                    {"start": 254, "end": 254, "residue": "N"},
                                    {"start": 255, "end": 255, "residue": "A"},
                                    {"start": 85, "end": 85, "residue": "R"},
                                    {"start": 283, "end": 283, "residue": "G"},
                                    {"start": 10, "end": 10, "residue": "K"},
                                    {"start": 275, "end": 275, "residue": "T"},
                                    {"start": 26, "end": 26, "residue": "M"},
                                    {"start": 31, "end": 31, "residue": "K"},
                                    {"start": 264, "end": 264, "residue": "L"},
                                    {"start": 270, "end": 270, "residue": "R"},
                                    {"start": 23, "end": 23, "residue": "A"},
                                    {"start": 271, "end": 271, "residue": "Q"},
                                    {"start": 281, "end": 281, "residue": "I"},
                                    {"start": 280, "end": 280, "residue": "E"},
                                    {"start": 251, "end": 251, "residue": "A"},
                                    {"start": 274, "end": 274, "residue": "I"},
                                    {"start": 282, "end": 282, "residue": "V"},
                                    {"start": 268, "end": 268, "residue": "K"},
                                    {"start": 120, "end": 120, "residue": "S"},
                                    {"start": 27, "end": 27, "residue": "V"},
                                    {"start": 258, "end": 258, "residue": "L"},
                                    {"start": 87, "end": 87, "residue": "L"},
                                    {"start": 20, "end": 20, "residue": "I"},
                                    {"start": 89, "end": 89, "residue": "G"},
                                    {"start": 90, "end": 90, "residue": "G"},
                                    {"start": 5, "end": 5, "residue": "K"},
                                    {"start": 128, "end": 128, "residue": "H"},
                                    {"start": 278, "end": 278, "residue": "L"},
                                    {"start": 124, "end": 124, "residue": "A"},
                                    {"start": 88, "end": 88, "residue": "C"},
                                    {"start": 285, "end": 285, "residue": "A"},
                                    {"start": 16, "end": 16, "residue": "S"},
                                    {"start": 121, "end": 121, "residue": "K"},
                                ],
                            },
                            {
                                "description": "epsilon subunit interface",
                                "numLocations": 10,
                                "siteLocations": [
                                    {"start": 136, "end": 136, "residue": "Q"},
                                    {"start": 123, "end": 123, "residue": "T"},
                                    {"start": 219, "end": 219, "residue": "T"},
                                    {"start": 222, "end": 222, "residue": "V"},
                                    {"start": 137, "end": 137, "residue": "V"},
                                    {"start": 134, "end": 134, "residue": "A"},
                                    {"start": 135, "end": 135, "residue": "A"},
                                    {"start": 138, "end": 138, "residue": "S"},
                                    {"start": 223, "end": 223, "residue": "R"},
                                    {"start": 139, "end": 139, "residue": "G"},
                                ],
                            },
                            {
                                "description": "delta subunit interface",
                                "numLocations": 11,
                                "siteLocations": [
                                    {"start": 219, "end": 219, "residue": "T"},
                                    {"start": 216, "end": 216, "residue": "L"},
                                    {"start": 41, "end": 41, "residue": "A"},
                                    {"start": 52, "end": 52, "residue": "V"},
                                    {"start": 45, "end": 45, "residue": "Y"},
                                    {"start": 44, "end": 44, "residue": "P"},
                                    {"start": 42, "end": 42, "residue": "S"},
                                    {"start": 51, "end": 51, "residue": "K"},
                                    {"start": 223, "end": 223, "residue": "R"},
                                    {"start": 220, "end": 220, "residue": "L"},
                                    {"start": 48, "end": 48, "residue": "T"},
                                ],
                            },
                        ],
                    }
                ],
                "source": "CDD",
            },
            {
                "signature": {
                    "accession": "TIGR01146",
                    "name": "ATPsyn_F1gamma",
                    "description": "ATP synthase F1 subunit gamma",
                    "type": "Family",
                    "signatureLibraryRelease": {
                        "library": "NCBIFAM",
                        "version": "17.0",
                    },
                    "entry": {
                        "accession": "IPR000131",
                        "name": "ATP_synth_F1_gsu",
                        "description": "ATP synthase, F1 complex, gamma subunit",
                        "type": "Family",
                        "parent": None,
                    },
                },
                "modelAccession": "TIGR01146",
                "score": 371.2,
                "evalue": 1.4e-107,
                "locations": [
                    {
                        "start": 1,
                        "end": 288,
                        "hmmStart": 1,
                        "hmmEnd": 286,
                        "hmmLength": 286,
                        "evalue": 1.6e-107,
                        "score": 371.1,
                        "fragments": [{"start": 1, "end": 288, "type": "CONTINUOUS"}],
                        "hmmBounds": "COMPLETE",
                        "envelopeStart": 1,
                        "envelopeEnd": 288,
                    }
                ],
                "source": "NCBIFAM",
            },
            {
                "signature": {
                    "accession": "NF004144",
                    "name": "PRK05621.1-1",
                    "description": "F0F1 ATP synthase subunit gamma",
                    "type": "Family",
                    "signatureLibraryRelease": {
                        "library": "NCBIFAM",
                        "version": "17.0",
                    },
                    "entry": None,
                },
                "modelAccession": "NF004144",
                "score": 509.2,
                "evalue": 0.0,
                "locations": [
                    {
                        "start": 1,
                        "end": 288,
                        "hmmStart": 1,
                        "hmmEnd": 287,
                        "hmmLength": 287,
                        "evalue": 0.0,
                        "score": 509.0,
                        "fragments": [{"start": 1, "end": 288, "type": "CONTINUOUS"}],
                        "hmmBounds": "COMPLETE",
                        "envelopeStart": 1,
                        "envelopeEnd": 288,
                    }
                ],
                "source": "NCBIFAM",
            },
            {
                "signature": {
                    "accession": "MF_00815",
                    "name": "ATP_synth_gamma_bact",
                    "description": "ATP synthase gamma chain [atpG]",
                    "type": "Family",
                    "signatureLibraryRelease": {
                        "library": "HAMAP",
                        "version": "2025_01",
                    },
                    "entry": {
                        "accession": "IPR000131",
                        "name": "ATP_synth_F1_gsu",
                        "description": "ATP synthase, F1 complex, gamma subunit",
                        "type": "Family",
                        "parent": None,
                    },
                },
                "modelAccession": "MF_00815",
                "locations": [
                    {
                        "start": 1,
                        "end": 288,
                        "cigarAlignment": "59M1D13M1D120M4D7M1I88M",
                        "fragments": [{"start": 1, "end": 288, "type": "CONTINUOUS"}],
                        "score": 36.834641,
                    }
                ],
                "source": "HAMAP",
            },
            {
                "signature": {
                    "accession": "PTHR11693",
                    "name": None,
                    "description": "ATP SYNTHASE GAMMA CHAIN",
                    "type": "Family",
                    "signatureLibraryRelease": {
                        "library": "PANTHER",
                        "version": "19.0",
                    },
                    "entry": {
                        "accession": "IPR000131",
                        "name": "ATP_synth_F1_gsu",
                        "description": "ATP synthase, F1 complex, gamma subunit",
                        "type": "Family",
                        "parent": None,
                    },
                },
                "modelAccession": "PTHR11693:SF22",
                "ancestralNode": "AN549",
                "evalue": 2.3e-62,
                "score": 223.1,
                "locations": [
                    {
                        "start": 1,
                        "end": 287,
                        "hmmStart": 46,
                        "hmmEnd": 345,
                        "hmmLength": 0,
                        "hmmBounds": "N_TERMINAL_COMPLETE",
                        "envelopeStart": 1,
                        "envelopeEnd": 288,
                        "fragments": [{"start": 1, "end": 287, "type": "CONTINUOUS"}],
                    }
                ],
                "source": "PANTHER",
            },
            {
                "signature": {
                    "accession": "PR00126",
                    "name": "ATPASEGAMMA",
                    "description": None,
                    "type": "Family",
                    "signatureLibraryRelease": {"library": "PRINTS", "version": "42.0"},
                    "entry": {
                        "accession": "IPR000131",
                        "name": "ATP_synth_F1_gsu",
                        "description": "ATP synthase, F1 complex, gamma subunit",
                        "type": "Family",
                        "parent": None,
                    },
                },
                "modelAccession": "PR00126",
                "evalue": 8.2e-37,
                "graphscan": "IIII",
                "locations": [
                    {
                        "start": 73,
                        "end": 92,
                        "pvalue": 4.75e-12,
                        "score": 50.8,
                        "motifNumber": 1,
                        "fragments": [{"start": 73, "end": 92, "type": "CONTINUOUS"}],
                    },
                    {
                        "start": 166,
                        "end": 183,
                        "pvalue": 2.22e-08,
                        "score": 35.33,
                        "motifNumber": 2,
                        "fragments": [{"start": 166, "end": 183, "type": "CONTINUOUS"}],
                    },
                    {
                        "start": 235,
                        "end": 254,
                        "pvalue": 1.87e-10,
                        "score": 59.9,
                        "motifNumber": 3,
                        "fragments": [{"start": 235, "end": 254, "type": "CONTINUOUS"}],
                    },
                    {
                        "start": 266,
                        "end": 287,
                        "pvalue": 3.94e-14,
                        "score": 71.73,
                        "motifNumber": 4,
                        "fragments": [{"start": 266, "end": 287, "type": "CONTINUOUS"}],
                    },
                ],
                "source": "PRINTS",
            },
            {
                "signature": {
                    "accession": "PS00153",
                    "name": "ATPASE_GAMMA",
                    "description": "ATP synthase gamma subunit signature",
                    "type": "Conserved_site",
                    "signatureLibraryRelease": {
                        "library": "PROSITE patterns",
                        "version": "2025_01",
                    },
                    "entry": {
                        "accession": "IPR023632",
                        "name": "ATP_synth_F1_gsu_CS",
                        "description": "ATP synthase, F1 complex, gamma subunit conserved site",
                        "type": "Conserved_site",
                        "parent": None,
                    },
                },
                "modelAccession": "PS00153",
                "locations": [
                    {
                        "start": 274,
                        "end": 287,
                        "cigarAlignment": "2M1I1M2I1M3I2M1I1M",
                        "fragments": [{"start": 274, "end": 287, "type": "CONTINUOUS"}],
                    }
                ],
                "source": "PROSITE patterns",
            },
            {
                "signature": {
                    "accession": "PF00231",
                    "name": "ATP-synt",
                    "description": "ATP synthase",
                    "type": "Domain",
                    "signatureLibraryRelease": {"library": "Pfam", "version": "38.0"},
                    "entry": {
                        "accession": "IPR000131",
                        "name": "ATP_synth_F1_gsu",
                        "description": "ATP synthase, F1 complex, gamma subunit",
                        "type": "Family",
                        "parent": None,
                    },
                },
                "modelAccession": "PF00231",
                "score": 361.1,
                "evalue": 1.7e-104,
                "locations": [
                    {
                        "start": 4,
                        "end": 288,
                        "hmmStart": 2,
                        "hmmEnd": 286,
                        "hmmLength": 286,
                        "evalue": 1.9e-104,
                        "score": 360.9,
                        "fragments": [{"start": 4, "end": 288, "type": "CONTINUOUS"}],
                        "hmmBounds": "C_TERMINAL_COMPLETE",
                        "envelopeStart": 3,
                        "envelopeEnd": 288,
                    }
                ],
                "source": "Pfam",
            },
            {
                "signature": {
                    "accession": "SSF52943",
                    "name": None,
                    "description": "ATP synthase (F1-ATPase), gamma subunit",
                    "type": "Homologous_superfamily",
                    "signatureLibraryRelease": {
                        "library": "SUPERFAMILY",
                        "version": "1.75",
                    },
                    "entry": {
                        "accession": "IPR035968",
                        "name": "ATP_synth_F1_ATPase_gsu",
                        "description": "ATP synthase, F1 complex, gamma subunit superfamily",
                        "type": "Homologous_superfamily",
                        "parent": None,
                    },
                },
                "modelAccession": "0036816",
                "evalue": 3.14e-96,
                "locations": [
                    {
                        "start": 2,
                        "end": 288,
                        "hmmLength": 272,
                        "fragments": [{"start": 2, "end": 288, "type": "CONTINUOUS"}],
                    }
                ],
                "source": "SUPERFAMILY",
            },
        ],
    },
    {
        "md5": "00D2ABB383FD824B362D1E15EA8FFED6",
        "matches": [
            {
                "signature": {
                    "accession": "G3DSA:3.30.160.60",
                    "name": None,
                    "description": "Classic Zinc Finger",
                    "type": "Homologous_superfamily",
                    "signatureLibraryRelease": {
                        "library": "CATH-Gene3D",
                        "version": "4.3.0",
                    },
                    "entry": None,
                },
                "modelAccession": "3mhsC02",
                "score": 37.2,
                "evalue": 7.1e-09,
                "locations": [
                    {
                        "start": 1,
                        "end": 29,
                        "hmmStart": 1,
                        "hmmEnd": 26,
                        "hmmLength": 31,
                        "evalue": 9.8e-09,
                        "score": 36.8,
                        "fragments": [{"start": 1, "end": 29, "type": "CONTINUOUS"}],
                        "hmmBounds": "COMPLETE",
                        "envelopeStart": 1,
                        "envelopeEnd": 29,
                    }
                ],
                "source": "CATH-Gene3D",
            },
            {
                "signature": {
                    "accession": "PTHR14649",
                    "name": None,
                    "description": "ZINC FINGER C2HC DOMAIN-CONTAINING PROTEIN 1C",
                    "type": "Family",
                    "signatureLibraryRelease": {
                        "library": "PANTHER",
                        "version": "19.0",
                    },
                    "entry": {
                        "accession": "IPR026104",
                        "name": "ZNF_C2HC_dom_1C",
                        "description": "Zinc finger C2HC domain-containing protein 1C",
                        "type": "Family",
                        "parent": None,
                    },
                },
                "modelAccession": "PTHR14649:SF1",
                "ancestralNode": "AN4",
                "evalue": 1.9e-12,
                "score": 58.7,
                "locations": [
                    {
                        "start": 1,
                        "end": 51,
                        "hmmStart": 391,
                        "hmmEnd": 441,
                        "hmmLength": 0,
                        "hmmBounds": "COMPLETE",
                        "envelopeStart": 1,
                        "envelopeEnd": 51,
                        "fragments": [{"start": 1, "end": 51, "type": "CONTINUOUS"}],
                    }
                ],
                "source": "PANTHER",
            },
            {
                "signature": {
                    "accession": "PS52027",
                    "name": "ZF_C2HC_C3H",
                    "description": "Zinc finger C2HC/C3H-type profile",
                    "type": "Domain",
                    "signatureLibraryRelease": {
                        "library": "PROSITE profiles",
                        "version": "2025_01",
                    },
                    "entry": {
                        "accession": "IPR049899",
                        "name": "Znf_C2HC_C3H",
                        "description": "Zinc finger, C2HC/C3H-type",
                        "type": "Domain",
                        "parent": None,
                    },
                },
                "modelAccession": "PS52027",
                "locations": [
                    {
                        "start": 1,
                        "end": 30,
                        "cigarAlignment": "30M",
                        "fragments": [{"start": 1, "end": 30, "type": "CONTINUOUS"}],
                        "score": 15.523909,
                    }
                ],
                "source": "PROSITE profiles",
            },
            {
                "signature": {
                    "accession": "PF13913",
                    "name": "zf-C2HC_2",
                    "description": "zinc-finger of a C2HC-type",
                    "type": "Domain",
                    "signatureLibraryRelease": {"library": "Pfam", "version": "38.0"},
                    "entry": None,
                },
                "modelAccession": "PF13913",
                "score": 34.8,
                "evalue": 3.1e-05,
                "locations": [
                    {
                        "start": 1,
                        "end": 25,
                        "hmmStart": 1,
                        "hmmEnd": 25,
                        "hmmLength": 25,
                        "evalue": 4.3e-05,
                        "score": 34.3,
                        "fragments": [{"start": 1, "end": 25, "type": "CONTINUOUS"}],
                        "hmmBounds": "COMPLETE",
                        "envelopeStart": 1,
                        "envelopeEnd": 25,
                    }
                ],
                "source": "Pfam",
            },
        ],
    },
    {
        "md5": "00CCA6BE1E3C4798846F7007903B1CEE",
        "matches": [
            {
                "signature": {
                    "accession": "G3DSA:2.170.40.20",
                    "name": None,
                    "description": "Human immunodeficiency virus 1, Gp160, envelope glycoprotein",
                    "type": "Homologous_superfamily",
                    "signatureLibraryRelease": {
                        "library": "CATH-Gene3D",
                        "version": "4.3.0",
                    },
                    "entry": {
                        "accession": "IPR036377",
                        "name": "Gp120_core_sf",
                        "description": "Gp120 core superfamily",
                        "type": "Homologous_superfamily",
                        "parent": None,
                    },
                },
                "modelAccession": "5vn3G01",
                "score": 193.7,
                "evalue": 1.6e-56,
                "locations": [
                    {
                        "start": 1,
                        "end": 120,
                        "hmmStart": 163,
                        "hmmEnd": 283,
                        "hmmLength": 400,
                        "evalue": 1.7e-56,
                        "score": 193.6,
                        "fragments": [{"start": 1, "end": 120, "type": "CONTINUOUS"}],
                        "hmmBounds": "COMPLETE",
                        "envelopeStart": 1,
                        "envelopeEnd": 120,
                    }
                ],
                "source": "CATH-Gene3D",
            },
            {
                "signature": {
                    "accession": "PF00516",
                    "name": "GP120",
                    "description": "Envelope glycoprotein GP120",
                    "type": "Domain",
                    "signatureLibraryRelease": {"library": "Pfam", "version": "38.0"},
                    "entry": {
                        "accession": "IPR000777",
                        "name": "HIV1_Gp120",
                        "description": "Human immunodeficiency virus 1, envelope glycoprotein Gp120",
                        "type": "Domain",
                        "parent": None,
                    },
                },
                "modelAccession": "PF00516",
                "score": 105.1,
                "evalue": 1.1e-26,
                "locations": [
                    {
                        "start": 1,
                        "end": 120,
                        "hmmStart": 260,
                        "hmmEnd": 396,
                        "hmmLength": 525,
                        "evalue": 1.2e-26,
                        "score": 104.9,
                        "fragments": [{"start": 1, "end": 120, "type": "CONTINUOUS"}],
                        "hmmBounds": "INCOMPLETE",
                        "envelopeStart": 1,
                        "envelopeEnd": 120,
                    }
                ],
                "source": "Pfam",
            },
            {
                "signature": {
                    "accession": "SSF56502",
                    "name": None,
                    "description": "gp120 core",
                    "type": "Homologous_superfamily",
                    "signatureLibraryRelease": {
                        "library": "SUPERFAMILY",
                        "version": "1.75",
                    },
                    "entry": {
                        "accession": "IPR036377",
                        "name": "Gp120_core_sf",
                        "description": "Gp120 core superfamily",
                        "type": "Homologous_superfamily",
                        "parent": None,
                    },
                },
                "modelAccession": "0053728",
                "evalue": 1.09e-57,
                "locations": [
                    {
                        "start": 1,
                        "end": 120,
                        "hmmLength": 339,
                        "fragments": [{"start": 1, "end": 120, "type": "CONTINUOUS"}],
                    }
                ],
                "source": "SUPERFAMILY",
            },
        ],
    },
]
single_responses = {
    200: {
        "description": "Success",
        "content": {"application/json": {"example": matches[0]}},
    }
}
batch_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {"example": [{**m, "found": True} for m in matches]}
        },
    }
}
