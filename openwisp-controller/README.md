## Support for ZeroTier VPN backend

1. Extending ZeroTier backend created in netjsonconfig to `vpn_backends.py`.
2. Adding vpn backend ZeroTier to `settings.py` i.e. settings.VPN_BACKENDS
3. Change the AbstractVpn and AbstractVpnClient to setup ZeroTier networks.
4. Generation of identity secret and identity public present in `/var/lib/zerotier-one`.

![zerotier-one-files](../images/identity.png)

5. We can use tool [zerotier-idtool](https://man.archlinux.org/man/community/zerotier-one/zerotier-idtool.1.en) to generate these identity secrets.

```
zerotier-idtool generate identity.secret identity.public
```
6. Changing templates to automatic generate ZeroTier VPN backend configuration.
