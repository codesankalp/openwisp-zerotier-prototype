# OpenWISP ZeroTier ProtoType

![gsoc_openwisp](./images/gsoc_openwisp.png)

### Deliverables and explanation with prototype:

1. Support for ZeroTier in netjsonconfig:
    - Capability for generating ZeroTier configuration in OpenWrt backend.
    - ZeroTier backend that generates network configuration accepted by REST API endpoints of the ZeroTier Controller.
    - Documentation for generating configuration for OpenWrt and ZeroTier Controller using netjsonconfig.

    **Explanation and prototype is inside [netjsonconfig](https://github.com/codesankalp/openwisp-zerotier-prototype/tree/master/netjsonconfig)**


2. Add ZeroTier as a VPN backend in OpenWISP Controller.
    - Add automatic generation of templates for ZeroTier VPN backend similar to OpenVPN and WireGuard VPN backends.
    - Integrate ZeroTier Controller APIs in OpenWISP Controller to allow managing networks directly from OpenWISP.
    - Write a step by step documentation which explains how to set up and use the new ZeroTier VPN backend with a device.

    **Explanation and prototype is inside [openwisp-controller](https://github.com/codesankalp/openwisp-zerotier-prototype/tree/master/openwisp-controller)**

3. Add a parser in OpenWISP Network Topology that can parse ZeroTier peer information.
    - Write documentation for using this parser to generate topology from data received from multiple devices.

    **Explanation and prototype is inside [openwisp-network-topology](https://github.com/codesankalp/openwisp-zerotier-prototype/tree/master/openwisp-network-topology)**

4. Achieve at least 99% test coverage for the code added for this feature.
