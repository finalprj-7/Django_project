
window.onload =function() {

    var element = document.getElementById("chatroom_box");
    element.scrollIntoView(false);

}

  function autoResize() {
    const input = document.getElementById('chat-message-input');
    input.style.height = 'auto'; // Reset the height to auto to calculate the actual height needed
    input.style.height = (input.scrollHeight) + 'px'; // Set the height to the calculated height
  }

  function calcTextareaHeight(e) {
    e.style.height = 'auto'
    e.style.height = `${e.scrollHeight}px`
}


//
// const scrollToBottom = () => {
//     window.scrollTo(0, document.body.scrollHeight);
// };
//
// // 페이지가 로드될 때 스크롤을 하단으로 이동
// window.onload = scrollToBottom;
//
// setTimeout(function() {
//                 window.scrollTo(0, document.body.scrollHeight);
//             }, 500);
//
// // 일정 시간 간격으로 페이지를 스크롤
// setInterval(() => {
//     scrollToBottom();
// }, 3000); // 예: 3초마다 스크롤





//
//
// window.onload = function() {
//             window.scrollTo(0, document.body.scrollHeight);
//         };
//
// setTimeout(function() {
//                 window.scrollTo(0, document.body.scrollHeight);
//             }, 500);
//
//
// // const scrollToBottom = () => {
// //     window.scrollTo(0, document.body.scrollHeight);
// // };
//
// // 페이지가 로드될 때 스크롤을 하단으로 이동
// //window.onload = scrollToBottom;
//
//
// function scrollToBottoms() {
//     let objDiv = document.getElementsByClassName("chat-log-container");
//     objDiv.scrollTop = objDiv.scrollHeight;
// }
//
// // Add this below the function to trigger the scroll on load.
// scrollToBottoms();