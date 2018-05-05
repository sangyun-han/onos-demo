#!/usr/bin/env python

from mininet.topo import topo

class TestTopo(Topo):
    "mininet test topology"

    def __init__(self):
        "Create a topology"

        Topo.__init__(self)

         # add nodes, switches first...
        switch_25 = self.addSwitch( 's25' ) # 40.728270, -73.994483
        switch_1 = self.addSwitch( 's1' )  # 42.373730, -71.109734
        switch_2 = self.addSwitch( 's2' )  # 41.877461, -87.642892
        switch_3 = self.addSwitch( 's3' )  # 41.498928, -81.695217
        switch_4 = self.addSwitch( 's4' )  # 35.780150, -78.644026
        switch_5 = self.addSwitch( 's5' )  # 33.749017, -84.394168
        switch_6 = self.addSwitch( 's6' )  # 39.952906, -75.172278
        switch_7 = self.addSwitch( 's7' )  # 38.906696, -77.035509
        switch_8 = self.addSwitch( 's8' )  # 36.166410, -86.787305
        switch_9 = self.addSwitch( 's9' )  # 38.626418, -90.198143
        switch_10 = self.addSwitch( 's10' ) # 29.951475, -90.078434
        switch_11 = self.addSwitch( 's11' ) # 29.763249, -95.368332
        switch_12 = self.addSwitch( 's12' ) # 29.424331, -98.491745
        switch_13 = self.addSwitch( 's13' ) # 32.777665, -96.802064
        switch_14 = self.addSwitch( 's14' ) # 28.538641, -81.381110
        switch_15 = self.addSwitch( 's15' ) # 39.736623, -104.984887
        switch_16 = self.addSwitch( 's16' ) # 39.100725, -94.581228
        switch_17 = self.addSwitch( 's17' ) # 37.779751, -122.409791
        switch_18 = self.addSwitch( 's18' ) # 38.581001, -121.497844
        switch_19 = self.addSwitch( 's19' ) # 45.523317, -122.677768
        switch_20 = self.addSwitch( 's20' ) # 47.607326, -122.331786
        switch_21 = self.addSwitch( 's21' ) # 40.759577, -111.895079
        switch_22 = self.addSwitch( 's22' ) # 34.056346, -118.235951
        switch_23 = self.addSwitch( 's23' ) # 32.714564, -117.153528
        switch_24 = self.addSwitch( 's24' ) # 33.448289, -112.076299

        # ... and now hosts
        switch_25_host = self.addHost( 'h25' )
        switch_1_host = self.addHost( 'h1' )
        switch_2_host = self.addHost( 'h2' )
        switch_3_host = self.addHost( 'h3' )
        switch_4_host = self.addHost( 'h4' )
        switch_5_host = self.addHost( 'h5' )
        switch_6_host = self.addHost( 'h6' )
        switch_7_host = self.addHost( 'h7' )
        switch_8_host = self.addHost( 'h8' )
        switch_9_host = self.addHost( 'h9' )
        switch_10_host = self.addHost( 'h10' )
        switch_11_host = self.addHost( 'h11' )
        switch_12_host = self.addHost( 'h12' )
        switch_13_host = self.addHost( 'h13' )
        switch_14_host = self.addHost( 'h14' )
        switch_15_host = self.addHost( 'h15' )
        switch_16_host = self.addHost( 'h16' )
        switch_17_host = self.addHost( 'h17' )
        switch_18_host = self.addHost( 'h18' )
        switch_19_host = self.addHost( 'h19' )
        switch_20_host = self.addHost( 'h20' )
        switch_21_host = self.addHost( 'h21' )
        switch_22_host = self.addHost( 'h22' )
        switch_23_host = self.addHost( 'h23' )
        switch_24_host = self.addHost( 'h24' )

        # add edges between switch and corresponding host
        self.addLink( switch_25 , switch_25_host )
        self.addLink( switch_1 , switch_1_host )
        self.addLink( switch_2 , switch_2_host )
        self.addLink( switch_3 , switch_3_host )
        self.addLink( switch_4 , switch_4_host )
        self.addLink( switch_5 , switch_5_host )
        self.addLink( switch_6 , switch_6_host )
        self.addLink( switch_7 , switch_7_host )
        self.addLink( switch_8 , switch_8_host )
        self.addLink( switch_9 , switch_9_host )
        self.addLink( switch_10 , switch_10_host )
        self.addLink( switch_11 , switch_11_host )
        self.addLink( switch_12 , switch_12_host )
        self.addLink( switch_13 , switch_13_host )
        self.addLink( switch_14 , switch_14_host )
        self.addLink( switch_15 , switch_15_host )
        self.addLink( switch_16 , switch_16_host )
        self.addLink( switch_17 , switch_17_host )
        self.addLink( switch_18 , switch_18_host )
        self.addLink( switch_19 , switch_19_host )
        self.addLink( switch_20 , switch_20_host )
        self.addLink( switch_21 , switch_21_host )
        self.addLink( switch_22 , switch_22_host )
        self.addLink( switch_23 , switch_23_host )
        self.addLink( switch_24 , switch_24_host )

        # add edges between switches
        self.addLink( switch_25 , switch_1)
        self.addLink( switch_25 , switch_1)
        self.addLink( switch_25 , switch_1)
        self.addLink( switch_25 , switch_2)
        self.addLink( switch_25 , switch_6)
        self.addLink( switch_25 , switch_6)
        self.addLink( switch_25 , switch_7)
        self.addLink( switch_1 , switch_6)
        self.addLink( switch_2 , switch_3)
        self.addLink( switch_2 , switch_6)
        self.addLink( switch_2 , switch_9)
        self.addLink( switch_2 , switch_15)
        self.addLink( switch_2 , switch_16)
        self.addLink( switch_2 , switch_16)
        self.addLink( switch_2 , switch_17)
        self.addLink( switch_2 , switch_20)
        self.addLink( switch_2 , switch_21)
        self.addLink( switch_3 , switch_8)
        self.addLink( switch_3 , switch_9)
        self.addLink( switch_3 , switch_6)
        self.addLink( switch_4 , switch_5)
        self.addLink( switch_4 , switch_7)
        self.addLink( switch_5 , switch_7)
        self.addLink( switch_5 , switch_8)
        self.addLink( switch_5 , switch_9)
        self.addLink( switch_5 , switch_13)
        self.addLink( switch_5 , switch_13)
        self.addLink( switch_5 , switch_13)
        self.addLink( switch_5 , switch_14)
        self.addLink( switch_6 , switch_7)
        self.addLink( switch_8 , switch_9)
        self.addLink( switch_8 , switch_13)
        self.addLink( switch_9 , switch_13)
        self.addLink( switch_9 , switch_16)
        self.addLink( switch_9 , switch_22)
        self.addLink( switch_10 , switch_11)
        self.addLink( switch_10 , switch_13)
        self.addLink( switch_10 , switch_14)
        self.addLink( switch_11 , switch_12)
        self.addLink( switch_11 , switch_13)
        self.addLink( switch_11 , switch_14)
        self.addLink( switch_12 , switch_24)
        self.addLink( switch_12 , switch_13)
        self.addLink( switch_13 , switch_15)
        self.addLink( switch_13 , switch_15)
        self.addLink( switch_13 , switch_16)
        self.addLink( switch_13 , switch_16)
        self.addLink( switch_13 , switch_17)
        self.addLink( switch_13 , switch_22)
        self.addLink( switch_13 , switch_22)
        self.addLink( switch_15 , switch_16)
        self.addLink( switch_15 , switch_17)
        self.addLink( switch_15 , switch_17)
        self.addLink( switch_15 , switch_21)
        self.addLink( switch_16 , switch_17)
        self.addLink( switch_17 , switch_18)
        self.addLink( switch_17 , switch_19)
        self.addLink( switch_17 , switch_20)
        self.addLink( switch_17 , switch_21)
        self.addLink( switch_17 , switch_22)
        self.addLink( switch_17 , switch_22)
        self.addLink( switch_17 , switch_22)
        self.addLink( switch_18 , switch_21)
        self.addLink( switch_19 , switch_20)
        self.addLink( switch_21 , switch_22)
        self.addLink( switch_22 , switch_23)
        self.addLink( switch_22 , switch_23)
        self.addLink( switch_22 , switch_24)
        self.addLink( switch_22 , switch_24)
        self.addLink( switch_23 , switch_24)

topos = { 'att': ( lambda: TestTopo() ) }

if __name__ == '__main__':
    from onosnet import run
    run( TestTopo() )
