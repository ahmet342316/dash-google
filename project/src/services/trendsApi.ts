import axios from 'axios';

const API_BASE_URL = 'http://localhost:8050';

interface TrendsParams {
  keywords: string;
  startDate: string;
  endDate: string;
  country?: string;
}

export async function fetchTrendsData({ 
  keywords, 
  startDate, 
  endDate, 
  country = 'US' 
}: TrendsParams) {
  try {
    const response = await axios.post(`${API_BASE_URL}/trends`, {
      keywords,
      start_date: startDate,
      end_date: endDate,
      country
    });

    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.error || 'Failed to fetch trends data');
    }
    throw error;
  }
}