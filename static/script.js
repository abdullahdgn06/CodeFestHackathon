document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.querySelector("#sidebar");
    const hideSidebarBtn = document.querySelector(".hide-sidebar");
    const messageBox = document.querySelector("#message");

    // Sidebar toggle functionality
    hideSidebarBtn.addEventListener("click", function() {
        sidebar.classList.toggle("hidden");
        // Save sidebar state to localStorage
        localStorage.setItem('sidebarHidden', sidebar.classList.contains('hidden'));
    });

    // Restore sidebar state from localStorage
    const sidebarHidden = localStorage.getItem('sidebarHidden') === 'true';
    if (sidebarHidden) {
        sidebar.classList.add("hidden");
    }

    // Message box auto-resize
    if (messageBox) {
        messageBox.addEventListener("keyup", function() {
            messageBox.style.height = "auto";
            let height = messageBox.scrollHeight + 2;
            if (height > 200) {
                height = 200;
            }
            messageBox.style.height = height + "px";
        });
    }
});

function show_view( view_selector ) {
    document.querySelectorAll(".view").forEach(view => {
        view.style.display = "none";
    });

    document.querySelector(view_selector).style.display = "flex";
}

const new_chat_button = document.querySelector(".new-chat");
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
messageBox.addEventListener("keydown", function(e) {
    if (e.key === "Enter" && !e.shiftKey) { // Check if "Enter" is pressed (not Shift + Enter)
        e.preventDefault(); // Prevent the default behavior of creating a new line
        messageForm.dispatchEvent(new Event("submit")); // Trigger the form submit
    }
});
