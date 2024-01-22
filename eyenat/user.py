import pyinaturalist


class UserData:
    def __init__(self, id):
        self.id = id
        f = pyinaturalist.get_user_by_id(self.id)

        self.login = f['login']
        self.login_autocomplete = f['login_autocomplete']
        self.login_exact = f['login_exact']
        self.name = f['name']
        self.name_autocomplete = f['name_autocomplete']
        self.orcid = f['orcid']

        self.observations_count = f['observations_count']
        self.identifications_count = f['identifications_count']
        self.journal_posts_count = f['journal_posts_count']
        self.activity_count = f['activity_count']
        self.species_count = f['species_count']
        self.universal_search_rank = f['universal_search_rank']

        self.spam = f['spam']
        self.suspended = f['suspended']
        self.roles = f['roles']
        self.site_id = f['site_id']
        self.icon = f['icon']
        self.icon_url = f['icon_url']
        self.created_at = f['created_at']
