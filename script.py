import datetime

afHex = "151DDC"
t = datetime.datetime.now().strftime("%f\n%d.%m.%Y\n%X")
script = f"""
function updateContact(){{
	let update = new Date();
	let updateMs = update.valueOf();
	let updateStr = update.toLocaleDateString() + \"<br>\" + \
update.toLocaleTimeString();
	let updateCell = document.getElementById(\"{afHex}\").children[11];
	updateCell.style.backgroundImage = \"url(\'Media/afInSight.jpg\')\";
	updateCell.children[0].innerHTML = updateMs;
	updateCell.children[1].innerHTML = updateStr;
}}
"""
print(script)
print(t)