import axios from 'axios'
import React from "react";

class App extends React.Component {
    state = {details: []}

    componentDidMount() {
        let data;
        axios.get('http://127.0.0.1:8000/react/')
            .then(res => {
                // without pagination
                data = res.data.results;
                console.log(data)
                this.setState({
                    details: data
                })
            })
            .catch(err => {
                console.log(err)
            })
    }

    render() {
        return (
            <>
                <header>Data from django</header>
                <hr></hr>
                {
                    this.state.details.map((output, id) => (
                        <div key={id}>
                            <div>
                               <span>Employee name:</span> <h2>{output.employee}</h2>
                                <span>Department name:</span><h3>{output.department}</h3>
                            </div>
                        </div>
                    ))
                }
            </>
        )
    }
}

export default App;
