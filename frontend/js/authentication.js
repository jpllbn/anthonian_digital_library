document.querySelector('form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const login = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    try {
      // Request access token
      const tokenRes = await fetch('http://127.0.0.1:8000/token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ username: login, password: password })
      });
      if (!tokenRes.ok) throw new Error('Invalid credentials');
      const { access_token } = await tokenRes.json();

      // Fetch current user data
      const userRes = await fetch('http://127.0.0.1:8000/users/me/', {
        headers: { 'Authorization': `Bearer ${access_token}` }
      });
      if (!userRes.ok) throw new Error('Failed to fetch user data');
      const userData = await userRes.json();
      console.log('Logged in user:', userData);
      // Display user info or redirect
      alert('Welcome, ' + userData.username + '! Role: ' + userData.role);
    } catch (err) {
      alert(err.message);
    }
  });