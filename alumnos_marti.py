def create_students_ldif(filename, class_name, num_students, base_dn):
    """Generates an LDIF file for a given class and number of students."""

    try:
        with open(filename, "w") as f:
            for i in range(1, num_students + 1):
                student_dn = f"uid=alumno{i},ou={class_name},{base_dn}"
                ldif_content = f"""# Student {i} in class {class_name}
dn: {student_dn}
changetype: add
objectClass: inetOrgPerson
uid: alumno{i}
sn: Student{i}
givenName: Alumno{i}
cn: Alumno{i} Student
mail: alumno{i}@example.com
ou: {class_name}
"""
                f.write(ldif_content)
                f.write("\n")  # Adding an empty line between entries for clarity
            print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Example usage:
filename = "alumnos_marti.ldif"  # Name of the LDIF file
class_name = "1ESOC"  # Class name
num_students = 20  # Number of students to generate
base_dn = "dc=marti,dc=org"  # Base DN defined in docker-compose.yml (same as LDAP_BASE_DN)

create_students_ldif(filename, class_name, num_students, base_dn)
