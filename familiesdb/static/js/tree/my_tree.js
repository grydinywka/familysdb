var js_rel = parseForDjango("{{ allRelatives|jsonify }}");
// make a new graph
var graph = new Springy.Graph();

// make some nodes
var father = graph.newNode({label: js_rel[1].fields.first_name});
var son = graph.newNode({label: 'Sergiy'});
var son2 = graph.newNode({label: 'Victor'});

// connect them with an edge
graph.newEdge(father, son);
graph.newEdge(father, son2);

var layout = new Springy.Layout.ForceDirected(
  graph,
  0, // Spring stiffness
  0, // Node repulsion
  0 // Damping
);

$('#my_tree').springy(
    {
        graph:  graph,
        layout: layout
    }
);