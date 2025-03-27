#!/bin/bash
STADY=$1

export TELEGRAM_BOT_TOKEN="6724221333:AAGgbjHR1-xRmBev8AJ5SwPGBorMK7OaUNc"
export TELEGRAM_USER_ID1="584856317"
export TELEGRAM_USER_ID2="1869880754"

export TIME=60 

sleep 5

URL="https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage"
#TEXT="Deploy status: $1%0A%0AProject:+$CI_PROJECT_NAME%0AStatus:+$CI_JOB_STATUS%0AURL:+$CI_PROJECT_URL/pipelines/$CI_PIPELINE_ID/%0ABranch:+$CI_COMMIT_REF_SLUG"

if [ "$CI_JOB_STATUS" == "success" ]; then
  MESSAGE="🤩🤩🤩 Стадия $STADY $CI_JOB_NAME прошла успешно! Ура! Можно радоваться! 🎉🎉🎉 $CI_PROJECT_URL/pipelines"
else
  MESSAGE="😭😭😭 Стадия $STADY $CI_JOB_NAME к сожалению не прошла! Попробуй все исправить и запустить еще раз! Ты все равно молодец! 💪💪💪 $CI_PROJECT_URL/pipelines"
  fi

curl -s --max-time $TIME -d "chat_id=$TELEGRAM_USER_ID1&disable_web_page_preview=1&text=$MESSAGE" $URL > /dev/null

curl -s --max-time $TIME -d "chat_id=$TELEGRAM_USER_ID2&disable_web_page_preview=1&text=$MESSAGE" $URL > /dev/null
