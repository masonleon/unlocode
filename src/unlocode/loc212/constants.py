"""
United Nations Code for Trade and Transport Locations
Recommendation No. 16
Revision 4 - 2020 Edition
United Nations Centre for Trade Facilitation and Electronic Business (UN/CEFACT)
https://unece.org/sites/default/files/2020-12/ECE-TRADE-459E.pdf
"""


DELIMITER = ","

"""
Section: II. B.
Pages: 3-4
"""
ENCODING = "ISO-8859-1"

"""
Section: II. D. 3.
Pages: 5-7
"""
UNLOCODE_FUNCTION_ATTRIBUTES_CODES = [
    {
        "Code"          : "1",
        "Function"      : "Maritime transport (sea port or maritime port)", 
        "Definition"    : "Any location with permanent facilities at which seagoing vessels can load or discharge cargo moving in maritime traffic."
    },
    {
        "Code"          : "2",
        "Function"      : "Rail transport", 
        "Definition"    : "Any location that has one or more railway terminals like cargo terminals or train stations (excluding passenger terminals). Specific terminals located inside a location shall not be considered individually as a location."
    },
    {
        "Code"          : "3",
        "Function"      : "Road transport", 
        "Definition"    : "Any location that is connected to other ones by means of roads. Specific terminals located inside a location shall not be considered individually as a location."
    },
    {
        "Code"          : "4",
        "Function"      : "Air transport (airport) or space transport (spaceport)", 
        "Definition"    : "Any location with permanent facilities at which aircraft can load or discharge cargo moving in air traffic."
    },
    {
        "Code"          : "5",
        "Function"      : "International Mail Processing Centre (IMPC) recognized by the Universal Postal Union (UPU)", 
        "Definition"    : "A mail processing facility, recognized by UPU, that has significance for the processing of inter-operator mail, either because they generate or receive dispatches or because they act as transit centres for mail exchanged between other IMPCs. Each IMPC has a well-defined physical location, is operated by or under the responsibility of a single organization and handles a specific set of mail flows. (This was known as a postal exchange office in the former edition of the Recommendation.)"
    },
    {
        "Code"          : "6",
        "Function"      : "Multimodal transport facility", 
        "Definition"    : "Any location where one or more of the below facilities can be found: \n\nInland Clearance Depot (ICD): a multimodal transport facility, other than a sea port or an airport, which is approved by a competent body, equipped with fixed installations and offering services for the handling and temporary storage of any kind of goods (including containers) carried under customs transit by any applicable mode of transport, placed under customs control and, with customs and other agencies, competent to clear goods for home use, warehousing, temporary admission, re-export, temporary storage for onward transit and outright export. (Definition applies also to synonyms like Dry Port, Inland Clearance Terminal, etc.) \n\nContainer Depot: a multimodal transport facility which offers services for storage, repair and maintenance of containers. \n\nInland freight terminal: a multimodal transport facility, other than a sea port or an airport, operated on a common-user basis, at which trade cargo is received or dispatched."
    },
    {
        "Code"          : "7",
        "Function"      : "Fixed Transport Installation (oil pipeline terminal, electric power lines, ropeway terminals, etc.)", 
        "Definition"    : "Any location with permanent facilities to load or discharge cargo that doesn’t fit in the previous definitions (e.g. oil platform)."
    },
    {
        "Code"          : "8",
        "Function"      : "Inland water transport (river ports, and lake ports)", 
        "Definition"    : "Any location with permanent facilities at which vessels can load or discharge cargo moving in inland waterway traffic."
    },
    {
        "Code"          : "0",
        "Function"      : "Not officially functional", 
        "Definition"    : "Digit \"0\" means that the criteria for inclusion apply, but that no information is available or used which is recognized by the competent authority regarding the specific transport mode or function(s) of the location."
    },
    {
        "Code"          : "B",
        "Function"      : "Cross Border (former code; not to be used)", 
        "Definition"    : "Any location that is located on the border with other countries. Specific border-crossing points located inside a location shall not be considered individually as a location."
    },
    {
        "Code"          : "A",
        "Function"      : "Special Economic Zone (SEZ)", 
        "Definition"    : "Any geographic region that has economic laws different from a country's typical economic laws for the purposes of trade operations and duties and tariffs."
    }    
]

"""
Section: II. D. 4.
Pages: 7-8
"""
UNLOCODE_STATUS_ATTRIBUTES_CODES = [
    {
        "Code"      : "AM",
        "Function"  : "Approved by the UN/LOCODE maintenance team consisting of the Secretariat, UN/CEFACT experts and representatives of the competent authorities."
    },
    {
        "Code"      : "RL",
        "Function"  : "Recognized location - Existence and representation of location name confirmed by check against nominated gazetteer or other reference work, but the relevance to international trade is not confirmed."
    },
    {
        "Code"      : "RQ",
        "Function"  : "Request under consideration – Maintenance procedure will indicate \"retained\" or special requests by the user community. Until the request has been validated, it should not be used in international electronic communication."
    },
    {
        "Code"      : "XX",
        "Function"  : "Entry that will be removed from the next issue of UN/LOCODE."
    }
]

UNLOCODE_LEGACY_STATUS_ATTRIBUTES_CODES = [
    {
        "Code"      : "AA",
        "Function"  : "Approved by competent national government agency"
    },
    {
        "Code"      : "AC",
        "Function"  : "Approved by Customs Authority"
    },
    {
        "Code"      : "AF",
        "Function"  : "Approved by national facilitation body"
    },
    {
        "Code"      : "AI",
        "Function"  : "Code adopted by international organization (IATA or ECLAC)"
    },
    {
        "Code"      : "AS",
        "Function"  : "Approved by national standardization body"
    },
    {
        "Code"      : "AQ",
        "Function"  : ""
    },
    {
        "Code"      : "RN",
        "Function"  : "Request from credible national sources for locations in their own country"
    }
]

"""
Section: Annex II. I.
Pages: 12
"""
CHANGE_INDICATION_LIST=[
    {
        "Change Indication" : "X",
        "Description"       : "Marked for deletion in the next issue"
    },
    {
        "Change Indication" : "#",
        "Description"       : "Change in the location name"
    },
    {
        "Change Indication" : "¦",
        "Description"       : "Other change in the entry"
    },
    {
        "Change Indication" : "+",
        "Description"       : "Entry added to the current issue"
    },
    {
        "Change Indication" : "=",
        "Description"       : "Reference entry"
    },
    {
        "Change Indication" : "!",
        "Description"       : "Retained for certain entries in the US code list (“controlled duplications”)"
    },
]

"""
Section: Annex II. IV.
Pages: 14
"""
ACCEPTABLE_DIACRITICS_AND_CONVERSION=[
    {
        # À, Á, Â, Ã, Ä, Å, Æ A
        "Substitute"    : "A",
        "Diacritic"     : ["À", "Á", "Â", "Ã", "Ä", "Å", "Æ"]
    },
    {
        # Ç C
        "Substitute"    : "C",
        "Diacritic"     : ["Ç"]
    },
    {
        # È, É, Ê, Ë E
        "Substitute"    : "E",
        "Diacritic"     : ["È", "É", "Ê", "Ë"]
    },
    {
        # Ì, Í, Î, Ï I
        "Substitute"    : "I",
        "Diacritic"     : ["Ì", "Í", "Î", "Ï"]
    },
    {
        # Ñ N
        "Substitute"    : "N",
        "Diacritic"     : ["Ñ"]
    },
    {
        # Ò, Ó, Ô, Õ, Ö, Ø O
        "Substitute"    : "O",
        "Diacritic"     : ["Ò", "Ó", "Ô", "Õ", "Ö", "Ø"]
    },
    {
        # Ù, Ú, Û, Ü U
        "Substitute"    : "U",
        "Diacritic"     : ["Ù", "Ú", "Û", "Ü"]
    },
    {
        # Ý Y
        "Substitute"    : "Y",
        "Diacritic"     : ["Ý"]
    },
    {
        # à, á, â, ã, ä, å, æ a
        "Substitute"    : "a",
        "Diacritic"     : ["à", "á", "â", "ã", "ä", "å", "æ"]
    },
    {
        # ç c
        "Substitute"    : "c",
        "Diacritic"     : ["ç"]
    },
    {
        # è, é, ê, ë e
        "Substitute"    : "e",
        "Diacritic"     : ["è", "é", "ê", "ë"]
    },
    {
        # ì, í, î, ï i
        "Substitute"    : "i",
        "Diacritic"     : ["ì", "í", "î", "ï"]
    },
    {
        # ñ n
        "Substitute"    : "n",
        "Diacritic"     : ["ñ"]
    },
    {
        # ò, ó, ô, õ, ö, ø o
        "Substitute"    :  "o",
        "Diacritic"     : ["ò", "ó", "ô", "õ", "ö", "ø"]
    },
    {
        # ù, ú, û, ü u
        "Substitute"    : "u",
        "Diacritic"     : ["ù", "ú", "û", "ü"]
    },
    {
        # ý, ÿ y
        "Substitute"    : "y",
        "Diacritic"     : ["ý", "ÿ"]
    }
]

"""
Section: Annex II. X.
Pages: 15
"""
TAGS_LIST=[
    {
        "Tag"               : "@Coo",
        "Description"       : "Change affecting or adding coordinates",
        "Change Indicator"  : "¦",
    },
    {
        "Tag"               : "@Fun",
        "Description"       : "Change affecting the function",
        "Change Indicator"  : "¦",
    },
    {
        "Tag"               : "@Sta",
        "Description"       : "Change of status",
        "Change Indicator"  : "¦",
    },
    {
        "Tag"               : "@Sub",
        "Description"       : "Addition or change of subdivision code",
        "Change Indicator"  : "¦",
    },
    {
        "Tag"               : "@Nam",
        "Description"       : "Change in the location name",
        "Change Indicator"  : "#",
    },
    {
        "Tag"               : "@Spe",
        "Description"       : "Correction of spelling of name",
        "Change Indicator"  : "#",
    },
]