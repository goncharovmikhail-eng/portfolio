#general
alias res="source ~/.zshrc"
alias ll='ls -lah'
alias req="rm -rf ./roles ; ansible-galaxy install -r requirements.yml -f -v"
alias md='mkdir -p'

function crsh() {
  local filename="${1}.sh"
  touch "$filename" 
  chmod 744 "$filename"
  echo '#!/bin/bash' > "$filename"
  nano "$filename"
}
function crpy() {
  local filename="${1}.py"
  touch "$filename"
  chmod 744 "$filename"
  echo '#!/usr/bin/env python3' > "$filename"
  nano "$filename"
}

hg(){
if [ ! -z "$3" ];then
history | grep -i $1 | grep -i $2 | grep -i $3
elif [ ! -z "$2" ];then
history | grep -i $1 | grep -i $2
else
history | grep -i $1
fi
}

c() {
  if [[ $1 == *"git"* ]]; then
    if [[ -n "$2" ]]; then
      git clone "$1" "$2" && cd "$2"
    else
      git clone "$1"
    fi
  else
    ssh "$1"
  fi
}

search_host() {
    # Функция для поиска машин, если передаётся один параметр,
    # и ОС, если имя ОС передаётся вторым параметром
    # Пример 1: search_host vostok
    # Пример 2: search_host run centos:7
    # Пример 2: search_host run bullseye
    # Для нормальной работы, в агенте д.б. ключ от используемого пользователя
    LIST_IP=("?" "?" "?" "...")
    LIST_NAME=("name1" "name2" "name3")
    SSH_USER='ssh_user'
    if [[ $2 ]]; then
        for ((i=1; i<=${#LIST_IP[@]}; i++)); do
            LIST_VM=$(ssh -o StrictHostKeyChecking=no $SSH_USER@$LIST_IP[$i] "sudo qm list | grep $1 | awk '{print \$2}' | xargs")
            LIST_VM_ARRAY=($(echo $LIST_VM | tr " " "\n" | xargs))
            RESULT=""
            for ((j=1; j<=${#LIST_VM_ARRAY[@]}; j++)); do
                if [[ ($(ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 -J $LIST_IP[$i] $SSH_USER@$LIST_VM_ARRAY[$j] "cat /etc/os-release | grep $2")) ]]; then
                    RESULT+=($LIST_VM_ARRAY[$j])
                fi
            done
            echo '----------------------------------------------------'
            for ((k=2; k<=${#RESULT[@]}; k++)); do
                echo 'на гипервизоре '$LIST_NAME[$i]' обнаружен '$2' на машине '$RESULT[$k]
            done
            echo '----------------------------------------------------'
        done
    else
        for ((n=1; n<=${#LIST_IP[@]}; n++)); do
            LIST_VM=$(ssh -o StrictHostKeyChecking=no $SSH_USER@$LIST_IP[$n] "hostname && sudo qm list | grep $1")
            echo $LIST_VM
            echo '----------------------------------------------------'
        done
    fi
}
