import falcon
from gm_api.api.mapping import Mapping, MappingResource
from gm_api.api.clusterids import Cluster
from gm_api.api.entitieslinks import Link
from wsgiref import simple_server  # NOQA
from gm_api.utils.logs import main_logger

do_map = Mapping()
do_clusterids = Cluster()
do_links = Link()

get_map = MappingResource()

gm_app = falcon.API()
gm_app.add_route('/map', do_map)
gm_app.add_route('/map/{mapID}', get_map)
gm_app.add_route('/clusterids', do_clusterids)
gm_app.add_route('/links', do_links)


if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 4302, gm_app)
    httpd.serve_forever()
    main_logger.info('App is running.')
