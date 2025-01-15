#git
alias gituponce="git fetch && git pull"
alias gs="git status"
gitdelb() {
if [ -z "$1" ]; then
  echo "Ошибка: не указано имя ветки для удаления."
  exit 1
fi
name_branch="origin/$1"
local_branch="$1"
if ! git show-ref --verify --quiet refs/heads/$local_branch; then
  echo "Ошибка: локальная ветка '$local_branch' не существует."
  exit 1
fi
echo "Переключаемся на ветку main..."
git checkout main
if [ $? -ne 0 ]; then
  echo "Ошибка: не удалось переключиться на ветку main."
  exit 1
fi
echo "Удаляем локальную ветку '$local_branch'..."
git branch -D $local_branch
if [ $? -ne 0 ]; then
  echo "Ошибка: не удалось удалить локальную ветку '$local_branch'."
  exit 1
fi
echo "Удаляем удаленную ветку '$name_branch'..."
git push origin --delete $local_branch
if [ $? -ne 0 ]; then
  echo "Ошибка: не удалось удалить удаленную ветку '$name_branch'."
  exit 1
fi
echo "Ветка '$name_branch' успешно удалена."
}
gitcheck() {
  local answer="full"
  find . -type d -name ".git" | sed 's/\/.git$//' | while IFS= read -r dir; do
    echo "Проверяем $dir..."
    cd "$dir" || { echo "Не удалось перейти в директорию $dir"; continue; }
    if [[ -n $(git status --porcelain) ]]; then
      echo "Незакоммиченные изменения найдены в $dir."
      git add . && git commit -m "$answer" && git push
      echo "Изменения закоммичены в $dir. с сообщением full. Не забывай комитить"
    else
      echo "Нет незакоммиченных изменений в $dir."
    fi
    cd - >/dev/null || exit
  done
}
gitcheck //закомментируйте, если не хотите пуша при запуске каждой сессии

gitnew() {
    if [ -z "$1" ]; then
        echo "Usage: git_init_push <repository_url>"
        return 1
    fi

    git init
    touch .gitignore README.md
    git add .
    git commit -m "first commit"
    git branch -M main
    git remote add origin "$1"
    git push -u origin main
}

gitpush() {
    if [ -z "$1" ]; then
        echo "describe the changes"
        return 1
    fi
    git add .
    git commit -m "$1"
    git push
}
gitupdate() {
  find . -type d -name ".git" | sed 's/\/.git$//' | while IFS= read -r dir; do
    echo "Проверяем $dir..."
    cd "$dir" || { echo "Не удалось перейти в директорию $dir"; continue; }
    if git fetch && git pull; then
      echo "Обновление $dir выполнено успешно."
    else
      echo "Ошибка обновления $dir."
    fi
    
    cd - >/dev/null || exit
  done
}
gitupdate //закомментируйте, если не хотите обновления локальных репозиториев при каждой новой сессии
