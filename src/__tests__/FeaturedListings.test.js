// src/__tests__/FeaturedListings.test.js
import { render, screen, waitFor } from "@testing-library/react";
import axios from "axios";
import FeaturedListings from "../components/FeaturedListings";

jest.mock("axios");

test("renders featured listings", async () => {
  const mockListings = [
    { id: 1, title: "Luxury Villa", price: 1000000, location: "Malibu", image: "/villa.jpg" },
    { id: 2, title: "Urban Apartment", price: 500000, location: "New York", image: "/apartment.jpg" },
  ];

  axios.get.mockResolvedValueOnce({ data: mockListings });

  render(<FeaturedListings />);
  await waitFor(() => {
    expect(screen.getByText("Luxury Villa")).toBeInTheDocument();
    expect(screen.getByText("Urban Apartment")).toBeInTheDocument();
  });
});
