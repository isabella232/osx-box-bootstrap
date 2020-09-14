require 'json'

CONFIG_json_content = {
	command: 'echo "Hello: ${T_KEY}!"',
	environments: [
		key: "T_KEY",
		value: "test value, with equal = sign, for test"
	]
}

puts JSON.generate(CONFIG_json_content)
