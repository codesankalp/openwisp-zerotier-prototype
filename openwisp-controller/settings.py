from django.conf import settings

settings.VPN_BACKENDS += [
    ('openwisp_controller.vpn_backends.ZeroTier', 'ZeroTier'),
]
