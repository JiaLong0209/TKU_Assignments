let inputs = document.querySelectorAll('.input_box');
let outputs = document.querySelectorAll('.output_box');
let saveBtn = document.querySelector('#saveBtn');
let IQ = document.querySelector('#IQ');
IQ.onchange = () => document.querySelector('#IQ_value').textContent = IQ.value
saveBtn.onclick = () => outputs.forEach((e, i) => {
        let target = [].filter.call(inputs[i].childNodes, (node) => node.tagName == "INPUT")
        e.children[0].innerHTML = target.length > 1 ? [].filter.call(target, (item) => item.checked).map(checked => checked.id) : target[0].value;
    })