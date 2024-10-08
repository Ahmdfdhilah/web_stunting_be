from pyramid.config import Configurator
# from pyramid.authorization import ACLAuthorizationPolicy
# from pyramid.authentication import AuthTktAuthenticationPolicy


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('.middleware')
        config.include('.models')
        config.include('.routes')

        config.scan()
    return config.make_wsgi_app()