const path = require('path');

module.exports = {
    entry: './static/scripts/index.js',

    output: {
        path: path.resolve('static/dist'),
        filename: 'index_bundle.js',
    },

    module: {
        loaders: [
            { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
            { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ },
        ]
    }
}