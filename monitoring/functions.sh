#/bin/bash
function ii() {
    RED='\e[31m' # Красный цвет
    NC='\e[0m'   # Сброс цвета
    # время
    echo -e "${RED}Дата:${NC} $(date '+%d.%m.%Y %H:%M:%S')"
    echo -e "${RED}Время с последней перезагрузки:${NC} $(uptime -p)"
    
    # общая информация
    echo -e "${RED}$HOSTNAME ($(hostname -f))${NC}, ОС: $(grep -E '^PRETTY_NAME=' /etc/os-release | cut -d= -f2 | tr -d '\"' || lsb_release -d | cut -f2)"
    echo -e "${RED}Ядро:${NC} $(uname -r), ${RED}Архитектура:${NC} $(uname -m)"
    echo -e "${RED}Ядер:${NC} $(nproc), ${RED}Загрузка CPU:${NC} $(top -b -n1 | grep 'load average' | awk '{print $10, $11, $12}')"
    echo -e "${RED}Оперативная память:${NC} $(free -h | grep Mem | awk '{print $3 "/" $2}')"
    
    # топ-5 процессов
    echo -e "${RED}Топ-5 процессов по CPU/RAM:${NC}"
    ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6
    
    # диски
    echo -e "${RED}Диски:${NC} $(df -hT | grep -E '^/dev/')"
    
    echo -e "${RED}Типы дисков и свободное место:${NC}"
    for disk in /sys/block/sd*; do
        disk_name=$(basename "$disk")
        disk_type=$(cat "$disk/queue/rotational")
        type=$([ "$disk_type" -eq 1 ] && echo "HDD" || echo "SSD")
        free_space=$(df -h | grep "/dev/$disk_name" | awk '{print $4}')
        echo "$disk_name: $type, свободно: ${free_space:-неизвестно}"
    done
    
    # сеть
    echo -e "${RED}Шлюз:${NC} $(ip route | awk '/default/ { print $3 }')"
    echo -e "${RED}Сетевые интерфейсы:${NC} $(ip -br a | grep -v LOOPBACK)"
    echo -e "${RED}Открытые порты:${NC} $(ss -tuln)"    
}

ii
