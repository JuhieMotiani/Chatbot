import React, {Component} from 'react';
import './Chatbubble.css';

class ChatBubble extends Component {
    
    who = ()=>{
        if(this.props.who === "userinput"){
            return "User: "
        }
        else{
            return "Bot: "
        }
    }

    render(){
        return(
            <React.Fragment>  
                <div className="chatbubble">
                    <p className="para"> <span style={{display: "inline-block", fontWeight: "bold", color: "lightskyblue"}}>{this.who()}</span>  {this.props.text}</p>
                </div>
                <br/>
            </React.Fragment>
        );
    }
}

export default ChatBubble;