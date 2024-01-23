from columnar import columnar

import user
import taxon
import observation


def user_search(id):
    uh = user.UserData(id)

    data = [['Username: ', '{}'.format(uh.login),
             'Observations: ', '{}'.format(uh.observations_count),
             'Account created: ', '{}'.format(uh.created_at.strftime("%c"))],
            ['Name: ', '{}'.format(uh.name),
             'Identifications: ', '{}'.format(uh.identifications_count),
             '', ''],
            ['Userid: ', '{}'.format(uh.id),
             'Species: ', '{}'.format(uh.species_count),
             '', '']]

    table = columnar(data, no_borders=True)
    print(table)
    return


def init_user_search(args):
    user_array = args.user.split(',')
    if len(user_array) > 1:
        [user_search(i) for i in user_array]
    else:
        user_search(user_array[0])
