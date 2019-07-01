from tethys_sdk.base import TethysAppBase, url_map_maker


class Amazonhqlocator(TethysAppBase):
    """
    Tethys app class for Amazon HQ Locator.
    """

    name = 'Amazon HQ Locator'
    index = 'amazonhqlocator:home'
    icon = 'amazonhqlocator/images/amazonHQ.gif'
    package = 'amazonhqlocator'
    root_url = 'amazonhqlocator'
    color = '#c97f10'
    description = 'Amazon HQ Locator'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='amazonhqlocator',
                controller='amazonhqlocator.controllers.home'
            ),

            UrlMap(
                name='service2',
                url='amazonhqlocator/service2',
                controller='amazonhqlocator.controllers.service2'
            ),
        )

        return url_maps
