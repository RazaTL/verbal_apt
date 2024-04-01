export type AssessmentResponse = string[];

export async function fetchAssessmentResponse(
  input: string
): Promise<AssessmentResponse> {
  const headers: Headers = new Headers();
  headers.set("Content-Type", "application/json");
  headers.set("Accept", "application/json");

  const request: RequestInfo = new Request("/", {
    method: "POST",
    headers,
    body: JSON.stringify({
      user_input: input,
    }),
  });

  const response = await fetch(request);
  const data = await response.json();
  return data;
}
