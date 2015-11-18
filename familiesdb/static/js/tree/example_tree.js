var graph = new Springy.Graph();

function randRGB() {
  return Math.floor(Math.random()*16777215).toString(16);
}

var kitten = graph.newNode({image: {src: 'http://www.placekitten.com/100/100'}});
var kittenNarrow= graph.newNode({image: {src: 'http://www.placekitten.com/100/100', width: 80}});
var cards = graph.newNode({image: {src: 'http://upload.wikimedia.org/wikipedia/commons/1/1a/5_Zener_cards_%28icon%29.jpg'}});

 var hello = graph.newNode({label: 'Springy.js image demo!'});
 var fromkit = graph.newNode({label: 'From placekitten.com'});
 var fromwik = graph.newNode({label: 'From Wikimedia Commons'});

graph.newEdge(hello, fromkit, {directional: false, color: randRGB()});
graph.newEdge(hello, fromwik, {directional: false, color: randRGB()});
graph.newEdge(fromkit, fromwik, {directional: false, color: randRGB()});
graph.newEdge(fromkit, kitten, {color: 'red'});
graph.newEdge(fromkit, kittenNarrow, {color: 'blue'});
graph.newEdge(fromwik, cards, {color: 'green'});


jQuery(function(){
  var springy = window.springy = jQuery('#springydemo').springy({
    graph: graph,
    nodeSelected: function(node){
      console.log('Node selected: ' + JSON.stringify(node.data));
    },
    repulsion: 150
  });
});