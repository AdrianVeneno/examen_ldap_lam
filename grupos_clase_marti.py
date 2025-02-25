def create_organizational_units_ldif(filename, ou_list, base_dn):
    """Generates an LDIF file for multiple organizational units."""
    
    try:
        with open(filename, "w") as f:
            for ou_name in ou_list:
                # Asegurarse de que haya un salto de línea al final de cada entrada
                ldif_content = f"""# organisational unit for {ou_name} department
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}

"""
                f.write(ldif_content)
            print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Example usage:
filename = "oueso1marti.ldif"  # Name of the LDIF file
ou_list = ["1ESOA", "1ESOB", "1ESOC", "1ESOD"]  # List of organizational units
base_dn = "dc=marti,dc=org"  # Base DN defined in docker-compose.yml (same as LDAP_BASE_DN)

create_organizational_units_ldif(filename, ou_list, base_dn)
