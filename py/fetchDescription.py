import requests

def get_wikidata_entity_id(search_term):
    """Get the Wikidata entity ID for a given search term."""
    url = f"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={search_term}&language=en&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('search', [])
        if results:
            return results[0].get('id')
    return None

def get_label(wikidata_id):
    """Get the label for a given Wikidata entity ID."""
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        entities = data.get('entities', {})
        entity = entities.get(wikidata_id, {})
        labels = entity.get('labels', {})
    if 'en' in labels:
        return labels['en']['value']
    return None

def get_parent_taxon_and_rank(wikidata_id):
    """Get the parent taxon and its rank for a given Wikidata entity ID."""
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        entity = data.get('entities', {}).get(wikidata_id, {})

        parent_taxon_id = None
        if 'P171' in entity.get('claims', {}):
            parent_taxon_claim = entity['claims']['P171'][0]
            if 'mainsnak' in parent_taxon_claim and 'datavalue' in parent_taxon_claim['mainsnak']:
                parent_taxon_id = parent_taxon_claim['mainsnak']['datavalue']['value']['id']

        rank_id = None
        if 'P105' in entity.get('claims', {}):
            rank_claim = entity['claims']['P105'][0]
            if 'mainsnak' in rank_claim and 'datavalue' in rank_claim['mainsnak']:
                rank_id = rank_claim['mainsnak']['datavalue']['value']['id']

        return parent_taxon_id, rank_id
    return None, None

def get_taxonomy(wikidata_id):
    """Get the complete taxonomy data for a given Wikidata entity ID."""
    taxonomy = {}
    current_id = wikidata_id

    while current_id:
        parent_taxon_id, rank_id = get_parent_taxon_and_rank(current_id)
        if rank_id:
            rank_label = get_label(rank_id)
            taxonomy[rank_label] = get_label(current_id)

        current_id = parent_taxon_id

    return taxonomy


def get_taxon_rank_label(wikidata_id):
    """Get the taxon rank label for a given Wikidata entity ID."""
    taxon_rank_labels = {
    'Q2': 'Domain',
    'Q756': 'Kingdom',
    'Q38348': 'Phylum',
    'Q37517': 'Class',
    'Q36602': 'Order',
    'Q368346': 'Suborder',
    'Q35409': 'Family',
    'Q37318': 'Subfamily',
    'Q34740': 'Genus'
    }
    return taxon_rank_labels.get(wikidata_id, None)

organism = "Lion"
wikidata_id = get_wikidata_entity_id(organism)
if wikidata_id:
    taxonomy = get_taxonomy(wikidata_id)
    print(f"Taxonomy for {organism}: {taxonomy}")
else:
    print("Wikidata entity ID not found.")
