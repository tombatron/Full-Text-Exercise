import React from 'react';
import Axios from 'axios';

export default class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            searchResults: []
        };

        this.updateSearchResults = this.updateSearchResults.bind(this);
    }

    updateSearchResults(results) {
        var data = !!results.data ? results.data : [];

        this.setState({
            searchResults: data
        });
    }

    onChange(event) {
        Axios.post('/search', {
            searchPhrase: event.target.value
        })

        .then(this.updateSearchResults)
        
        .catch(function (error) {
            console.log(`Error: ${error}`);
        });
    }

    render() {
        return (
            <div>
                <div style={{textAlign: 'center'}}>
                    <h1>Hello World</h1>
                </div>

                <div>
                    <input type="text" onChange={this.onChange.bind(this)} />
                </div>

                <SearchResults results={this.state.searchResults} />
            </div>
        )
    }
}

class SearchResults extends React.Component {
    renderSearchResult(searchResult) {
        return (
            <li key={searchResult}>{searchResult}</li>
        );
    }

    render() {
        return (
            <div>
                <ul>
                    {this.props.results.map(this.renderSearchResult)}
                </ul>
            </div>
        )
    }
}