//500 потому что максимум 500 в gs
function triggers() {
  for (var i = 0; i <= 10; i++){
  ScriptApp.newTrigger('clean_gmail')
    .timeBased()
    .onMonthDay(13)
    .atHour(i)
    .create();
  Logger.log('Триггер создан: ' + i);
  }
}

function clean_gmail() {
  let threads = GmailApp.getInboxThreads(0, 500);
  if (threads.length === 0) {
    Logger.log("Нет тредов для удаления.");
    return;
  }
  threads.forEach(thread => thread.moveToTrash());
  Logger.log(threads.length + " тредов отправлено в корзину.");
}
