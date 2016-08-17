var assert = require('assert');

var DEBUG = false;


function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}


function contract(graph, fromVertex, toVertex) {
    // merge fromVertex1 and toVertex1
    var vets = graph[fromVertex];

    // modified all edges connected to fromVertex to toVertex instead
    for (var i = 0; i < vets.length; i ++ ) {
        var vet = vets[i];
        // update the relevant adjacency lists
        var ajlist = graph[vet];

        // console.log("vet: ", vet);
        // console.log("graph[vet]: ", graph[vet]);
        assert(ajlist !== undefined);

        var start = 0;

        while (true) {
            start = ajlist.indexOf(fromVertex, start);
            if (start !== -1) {
                if (vet === toVertex)
                    // remove fromVertex from toVertex's adjacency list
                    ajlist.splice(start, 1);
                else
                    // replace fromVertex with toVertex
                    ajlist[start] = toVertex;
            } else
                break;
        }

        if (vet !== toVertex)
            // update the adjacency list of toVertex
            graph[toVertex].push(vet);
    }

    // remove the fromVertex and its connected edges completely
    delete graph[fromVertex];
}


var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('kargerMinCut.txt')
});


var graph = {};

lineReader.on('line', function (line) {
    var spl = line.trim().split('\t');
    graph[spl[0]] = spl.slice(1);
}).on('close', function () {
    var keys = Object.keys(graph);
    while (keys.length > 2) {
        fromVertex = keys[getRandomInt(0, keys.length)];
        toVertex = graph[fromVertex][getRandomInt(1, graph[fromVertex].length)];

        if (DEBUG)
            console.log('fromVertex: ', fromVertex, 'toVertex: ', toVertex);
        assert(fromVertex !== toVertex);

        contract(graph, fromVertex, toVertex);
        keys = Object.keys(graph);
    }

    assert(graph[keys[0]].length === graph[keys[1]].length);
    console.log(graph[keys[0]].length);
    if (DEBUG)
        console.log(graph);
});



// var graph = {
//     0: [1, 3],
//     1: [0, 2, 3],
//     2: [1, 3],
//     3: [0, 1, 2]
// };

// console.log(graph);

// var i = 0;
// var j = 3;
// contract(graph, i, j);
// assert.deepEqual(graph, {
//     1: [3, 2, 3 ],
//     2: [1, 3 ],
//     3: [1, 2, 1 ]
// });
// console.log(graph);


// i = 1;
// j = 3;
// contract(graph, i, j);
// assert.deepEqual(graph, {
//     2: [3, 3 ],
//     3: [2, 2 ]
// });
// console.log(graph);
