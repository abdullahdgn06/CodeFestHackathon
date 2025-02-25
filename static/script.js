const sidebar = document.querySelector("#sidebar");
const hide_sidebar = document.querySelector(".hide-sidebar");
const new_chat_button = document.querySelector(".new-chat");

hide_sidebar.addEventListener( "click", function() {
    sidebar.classList.toggle( "hidden" );
} );

const message_box = document.querySelector("#message");

message_box.addEventListener("keyup", function() {
    message_box.style.height = "auto";
    let height = message_box.scrollHeight + 2;
    if( height > 200 ) {
        height = 200;
    }
    message_box.style.height = height + "px";
});

function show_view( view_selector ) {
    document.querySelectorAll(".view").forEach(view => {
        view.style.display = "none";
    });

    document.querySelector(view_selector).style.display = "flex";
}

new_chat_button.addEventListener("click", function() {
    show_view( ".new-chat-view" );
});

document.querySelectorAll(".conversation-button").forEach(button => {
    button.addEventListener("click", function() {
        show_view( ".conversation-view" );
    })
});


// Also trigger form submit when send button is clicked
const sendButton = document.querySelector(".send-button");
sendButton.addEventListener("click", () => {
    messageForm.dispatchEvent(new Event("submit"));
});

// Allow sending the message by pressing "Enter"
message_box.addEventListener("keydown", function(e) {
    if (e.key === "Enter" && !e.shiftKey) { // Check if "Enter" is pressed (not Shift + Enter)
        e.preventDefault(); // Prevent the default behavior of creating a new line
        messageForm.dispatchEvent(new Event("submit")); // Trigger the form submit
    }
});
