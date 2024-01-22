import pyinaturalist


class TaxonData:
    def __init__(self, id):
        self.id = id
        f = pyinaturalist.get_taxon_by_id(self.id)['results'][0]

        """ The taxonomic rank of the taxon, ie: family, genus, species etc. """
        self.rank = f['rank']
        self.rank_level = f['rank_level']
        self.iconic_taxon_id = f['iconic_taxon_id']

        """ A list of integers of the taxon's ancestor IDs. """
        self.ancestor_ids = f['ancestor_ids']
        self.is_active = f['is_active']

        """ The taxon's scientific name.  """
        self.name = f['name']

        """ The integer id of the immediate parent taxon. """
        self.parent_id = f['parent_id']

        """ A forward-slash delimited string of the taxon's ancestor IDs. """
        self.ancestry = f['ancestry']

        """ A boolean of whether the taxon is extinct or not. """
        self.extinct = f['extinct']

        """ A dictionary containing information about the taxon's default photo,
            as displayed on the iNaturalist taxon page. """
        self.default_photo = f['default_photo']
        self.taxon_changes_count = f['taxon_changes_count']
        self.taxon_schemes_count = f['taxon_schemes_count']

        """ An integer count of the taxon's observations on iNat. """
        self.observations_count = f['observations_count']
        self.photos_locked = f['photos_locked']
        self.flag_counts = f['flag_counts']
        self.current_synonymous_taxon_ids = f['current_synonymous_taxon_ids']
        self.taxon_photos = f['taxon_photos']
        self.atlas_id = f['atlas_id']

        """ An integer count of species under the taxon (will be 0 for species taxons). """
        self.complete_species_count = f['complete_species_count']

        """ A URL to Wikipedia's page on the taxon. """
        self.wikipedia_url = f['wikipedia_url']
        self.complete_rank = f['complete_rank']
        self.iconic_taxon_name = f['iconic_taxon_name']

        """ The common name for the taxon. This is affected by locale. """
        self.preferred_common_name = f['preferred_common_name']
        self.ancestors = f['ancestors']
        self.children = f['children']
        self.conservation_statuses = f['conservation_statuses']
        self.conservation_status = f['conservation_status']
        self.listed_taxa_count = f['listed_taxa_count']
        self.listed_taxa = f['listed_taxa']
        self.wikipedia_summary = f['wikipedia_summary']
        self.vision = f['vision']
        self.created_at = f['created_at']
