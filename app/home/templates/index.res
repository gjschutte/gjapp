<!-- extend base layout -->
{% extends "base.html" %}

{% block content %}
	<h1>Hi, welcome</h1>
	<p>
	{{ spreuk.body }} - {{ spreuk.auteur }}
	</p>
<!--	<a href="{{ url_for('beheer') }}">Beheer</a>
	<a href="{{ url_for('analyse') }}">Gegevens computer</a> -->
{% endblock %}