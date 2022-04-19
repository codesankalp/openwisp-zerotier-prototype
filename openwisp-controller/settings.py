# other definitions

VPN_BACKENDS = get_settings_value(
    'VPN_BACKENDS',
    (
        ('openwisp_controller.vpn_backends.OpenVpn', 'OpenVPN'),
        ('openwisp_controller.vpn_backends.Wireguard', 'WireGuard'),
        ('openwisp_controller.vpn_backends.VxlanWireguard', 'VXLAN over WireGuard'),
        ('openwisp_controller.vpn_backends.ZeroTier', 'ZeroTier'),
    ),
)