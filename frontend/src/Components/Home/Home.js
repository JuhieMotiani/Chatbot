import React, { Component } from 'react';
import ChatBubble from '../Chatbubble/Chatbubble';
import './Home.css';
import axios from 'axios';


class Test extends Component {
    

    state = {
        messages: [],
        input: [],
    }

    constructor(props) {
        super(props);
        this.state = {
            messages: [],
            input: []
        }
        
        this.appendMessage = this.appendMessage.bind(this);
        
    }


    

    callFunc = () => {
        document.getElementById("button").style.display = "none";
        document.getElementById("chatbot").style.display = "inline-block";
    }

    appendMessage = () => {
        if (document.getElementById("inputval").value === "")
            console.log("No value entered")
        else
            this.setState({ messages: this.state.messages.concat(document.getElementById("inputval").value), input: this.state.input.concat("userinput")}, () => {
                this.appendResponse();
            });
            document.getElementById("inputval").value = "";
            
        
    }    

    appendResponse = async () => {        
        var index = this.state.input.lastIndexOf("userinput");
        var message = this.state.messages[index]

        const res = await axios.get('http://localhost:3000/output', { params:  {message}  });

        this.setState({ messages: this.state.messages.concat(res.data), input: this.state.input.concat("botinput")});
        
    }

    
    render() {
        var input = this.state.input;
        var message = this.state.messages;
        return (
            <React.Fragment>
                <button id="button" className="buttonStyle" onClick={this.callFunc}>Activate Assistant</button>
                <div id="chatbot">
                    <h2 className="heading">Welcome to ZipBooks' Virtual Assistant</h2>
                    <div className="chatSegment" id="chatSegment">
                        <div className="displayChatSegment" id="parent">
                            {   
                                this.state.input.map(function(input, index){
                                    return(<ChatBubble text={message[index]} who={input} />)    
                                })
                            }
                        </div>
                        
                        <div className="inputSegment">
                            <textarea type="text" id="inputval" placeholder="Enter Text Here!" className="inputText"></textarea>
                            <button id="sendButton" className="sendButtonStyle" onClick={this.appendMessage}>^</button>
                        </div>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}

export default Test;