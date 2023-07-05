// send a message to content.js to get article contents
function RequireContent() {
    chrome.tabs.query(
        { active: true, currentWindow: true },
        function (tabs) {
            chrome.tabs.sendMessage(
                tabs[0].id,
                { content: "1st" },
                // after get article contents, connect to backend web
                function (response) {
                    ConnectToBackend(response);
                }
            );
        }
    );
}

// send predictions to content.js
async function SecondMessage(r){
    chrome.tabs.query(
        { active: true, currentWindow: true },
        function(tabs){
            chrome.tabs.sendMessage(
                tabs[0].id,
                {content: r},
                function(response){
                console.log(response)
                }
            )
        }
    )  
}

// connect to backend which is on DigitalOcean droplet  
async function ConnectToBackend(content){
    fetch('http://128.199.218.40/test',{
      headers : {
        'Content-Type' : 'application/json'
      },
      method : 'POST', 
      body : JSON.stringify(content)
    })
    .then((response) => {
        return response.json();
    })
    .then((response) => {
        // after get the prediction from backend, send message to content.js again
        var x = response['message']
        SecondMessage(x)
    })
    .catch((error) => {
        console.log(`Error: ${error}`);
    })
}

// 待修改
// var flag = true

// chrome.runtime.onMessage.addListener(
//     function(message){
//         if(message.content == 'start'){
//             flag = true
//             chrome.tabs.reload()
//         }            
//         if(message.content == 'end'){
//             flag = false
//             chrome.tabs.reload()
//         }            
//     }
// )

// if open the Bahamut NCU page then submit a request to get article
chrome.tabs.onUpdated.addListener(
    function(tabId, changeInfo, tab){
        if(changeInfo.status === 'complete'){
            if (tab.url.includes('snA=4671705') && flag){
                RequireContent()
            }
        }        
    }
)