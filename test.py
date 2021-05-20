def volume_cylinder(radius, height):
    pi = 3.14
    volume = pi*radius**2*height
    return volume


def main():
    volume = volume_cylinder(12, 3)
    print(f"The volume is {volume:.2f}")


if __name__ == "__main__":
    main()
