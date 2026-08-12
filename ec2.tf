provider aws {
	alias : mumbai
	region: ap-south-1
		
	}

 resource aws_instance ec2 {
	ami: var.id
	instance_type: var.type
	key_pair: var.key
	}

