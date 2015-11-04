// make a new graph
var graph = new Springy.Graph();

// make some nodes
var father = graph.newNode({label: 'Kostyantin'});
var son = graph.newNode({label: 'Sergiy'});
var son2 = graph.newNode({label: 'Victor'});

// connect them with an edge
graph.newEdge(father, son);
graph.newEdge(father, son2);

$('#my_tree').springy({ graph: graph });

var layout = new Springy.Layout.ForceDirected(
  graph,
  400.0, // Spring stiffness
  400.0, // Node repulsion
  0.5 // Damping
);

var renderer = new Springy.Renderer(
  layout,
  function clear() {
    // code to clear screen
  },
  function drawEdge(edge, p1, p2) {
    // draw an edge
  },
  function drawNode(node, p) {
    // draw a node
  }
);

renderer.start();
