function escapeRegExp(string)
{
    const regex = /<.*?>/g;
    return string.replaceAll(regex, "");
}

// get Bahamut NCU's article content
function GetContent()
{
    var contents_withHTML = document.getElementsByClassName("c-article__content");
    var contents_withoutHTML = [];
    for(var i=0; i<contents_withHTML.length; i++)
    {
        var content = escapeRegExp(contents_withHTML[i].innerHTML);
        contents_withoutHTML.push(content);
    }
    return contents_withoutHTML;
}

// add predict result to the article
function AddLabel(m){
    var c = document.getElementsByClassName("c-article__content");
    if(c[0].getElementsByClassName("label").length>0)
        return
    else{
        for(var i=0; i<m.length; i++){
            var newtext = document.createElement("div")
            var label = '\n\n'
            label += '#'
            label += m[i][0]
            label += ' '
            newtext.textContent = label
            newtext.setAttribute('class', 'label')
            newtext.style.color = 'blue'
            c[i].appendChild(newtext)
        }
    }    
}


// get message from background.js
chrome.runtime.onMessage.addListener(function(message, sender, sendResponse){
    // first time message
    if(message.content == '1st'){
        var x = GetContent();
        sendResponse({ content: x});
    }
    // second message
    else{
        AddLabel(message['content'])
        sendResponse({ content: 'END'})
    }    
});




