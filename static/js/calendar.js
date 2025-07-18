// 超基础前端日历，支持本地心情签到（刷新后消失）！

const calendarDiv = document.getElementById('calendar');
const today = new Date();
const year = today.getFullYear();
const month = today.getMonth(); // 0~11

// 获取当月第一天是星期几，以及天数
const firstDay = new Date(year, month, 1).getDay();
const daysInMonth = new Date(year, month + 1, 0).getDate();

let html = '<table class="calendar-table"><tr>';
const weekDays = ['日', '一', '二', '三', '四', '五', '六'];
for (let d = 0; d < 7; d++) {
    html += `<th>${weekDays[d]}</th>`;
}
html += '</tr><tr>';

// 空位补齐
for (let d = 0; d < firstDay; d++) {
    html += '<td></td>';
}

for (let day = 1; day <= daysInMonth; day++) {
    const thisDate = `${year}-${month + 1}-${day}`;
    html += `<td data-date="${thisDate}" style="cursor:pointer">${day}</td>`;
    if ((firstDay + day) % 7 === 0) html += '</tr><tr>';
}
html += '</tr></table>';
calendarDiv.innerHTML = html;

// 点击签到（弹窗输入心情）
calendarDiv.querySelectorAll('td[data-date]').forEach(cell => {
    cell.onclick = () => {
        const mood = prompt(`请输入 ${cell.getAttribute('data-date')} 的心情:`);
        if (mood) cell.innerHTML = `${cell.innerText}<br><span style="font-size:0.9em;color:#e49acb">${mood}</span>`;
    };
});
