"""
Republic of Ireland
Munster Technological University 
Department of Computer Science
Student: Jose Lo Huang
Mininet Project - Topology with 3 switches and 2 nodes. 
"""

from mininet.topo import Topo

class MyTopo( Topo ): 
"""
This class creates a topology with 3 switches and 2 hosts. The paths will be:
* Path 1: h1 - s1 - s2 - h2
* Path 2: h1 - s1 - s3 - s2 - h2
"""
   def build( self ):
   "This function will create the architecture."
      # Add hosts and switches 
      h1 = self.addHost( 'h1' ) 
      h2 = self.addHost( 'h2' )

      s1 = self.addSwitch( 's1' ) 
      s2 = self.addSwitch( 's2' ) 
      s3 = self.addSwitch( 's3' )

      # Add links 
      self.addLink( s1, h1 ) 
      self.addLink( s1, s2 ) 
      self.addLink( s1, s3 ) 
      self.addLink( s2, s3 ) 
      self.addLink( s2, h2 )

# Create the topology invoking the MyTopo class 
topos = { 'mytopo': ( lambda: MyTopo() ) }


