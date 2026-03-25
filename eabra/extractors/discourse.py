from eabra.aggregators import aggregate_feature_dict

def extract(doc):
    """
    Extracts Discourse variables.
    Equivalent to FABRA Family: Discourse Variables
    """
    features = {}
    
    # Referential expressions
    # DISrefPN: Proportion of pronouns to all nouns.
    # We compute this per sentence (or document). Let's do per sentence, then aggregate.
    
    pron_props = []
    def_props = []
    dia_bingui = []
    dia_ppei1 = []
    dia_ppei2 = []
    
    quote_chars = {'"', "'", '“', '”', '‘', '’', '«', '»'}
    
    for sent in doc.sents:
        num_nouns = sum(1 for token in sent if token.pos_ == 'NOUN')
        num_prons = sum(1 for token in sent if token.pos_ == 'PRON')
        num_words = len([t for t in sent if not t.is_punct])
        
        # definite articles (the)
        num_def = sum(1 for token in sent if token.text.lower() == 'the' and token.pos_ == 'DET')
        
        if num_nouns > 0:
            pron_props.append(num_prons / num_nouns)
            def_props.append(num_def / num_nouns)
        else:
            pron_props.append(0.0)
            def_props.append(0.0)
            
        # Dialogue Variables
        # DISdiaBINGUI: Presence of dialogue quotes.
        num_quotes = sum(1 for token in sent if token.text in quote_chars)
        dia_bingui.append(1 if num_quotes > 0 else 0)
        
        # DISdiaPPEI1: Percentage of exclamation and question marks considering all sentence stops.
        num_excl_quest = sum(1 for token in sent if token.text in {'!', '?'})
        num_stops = sum(1 for token in sent if token.text in {'.', '!', '?'})
        if num_stops > 0:
            dia_ppei1.append((num_excl_quest / num_stops) * 100.0)
        else:
            dia_ppei1.append(0.0)
            
        # DISdiaPPEI2: Percentage of exclamation and question marks considering all sentence stops and colons.
        num_stops_colons = sum(1 for token in sent if token.text in {'.', '!', '?', ':'})
        if num_stops_colons > 0:
            dia_ppei2.append((num_excl_quest / num_stops_colons) * 100.0)
        else:
            dia_ppei2.append(0.0)
            
    # Aggregate
    features.update(aggregate_feature_dict('DISrefPN', pron_props))
    features.update(aggregate_feature_dict('DISrefDN', def_props))
    features.update(aggregate_feature_dict('DISdiaBINGUI', dia_bingui))
    features.update(aggregate_feature_dict('DISdiaPPEI1', dia_ppei1))
    features.update(aggregate_feature_dict('DISdiaPPEI2', dia_ppei2))
    
    return features
